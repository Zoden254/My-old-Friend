import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from . import models

# Create your views here.


def home(request):
    feeds = models.Feed.objects.all()
    return render(request, "home.html", {'feeds': feeds})

def nav(request):
            
    return render(request, "partials/nav.html", {'unread_nots': 0})
    

def notification_sync(request):
    if request.user.is_authenticated:
        unread_notifications = request.user.notifications.filter(read=False)
        unread_nots = len(unread_notifications)
        if unread_nots > 9:
            unread_nots = "9+"
        return render(request, "partials/notification.html", {'unread_nots': unread_nots})
    else:
        return render(request, "partials/notification.html")


def notification_box(request):
    notifications = request.user.notifications.filter(read=False)
    return render(request, "partials/notifications-box.html", {'notifications': notifications})

def login_view(request):
    #if 'HTTP_HX_REQUEST' in request.META:
    #    return render(request, "partials/login.html")
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome {user.first_name}")
            
            return redirect("admin_app:home")
        else:
            messages.error(request, "Invalid user.")
            return redirect('admin_app:login')
    return render(request, "full-login-page.html")


def logout_view(request):
    logout(request)
    return redirect('admin_app:home')
    
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST['f_name']
        lastname = request.POST['l_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if username not in models.User.objects.values_list('username', flat=True):
            new_user = models.User.objects.create_user(username=username, email=email, password=password, first_name=firstname, last_name=lastname)
        else:
            messages.error(request, "Username already used.")
            return redirect('admin_app:signup')
        
        return redirect('admin_app:login')
    
    if 'HTTP_HX_REQUEST' in request.META:
        return render(request, "partials/signup.html")
    return render(request, "full-signup-page.html")



def v_nav(request):
    return render(request, "partials/vertical-nav.html")

@login_required(login_url="admin_app:login")
def friends(request):
    suggestions = models.User.objects.exclude(id=request.user.id).exclude(id__in=request.user.friends.values_list('id', flat=True))
    suggestions = suggestions.exclude(id__in=request.user.friendrequest_received.values_list('from_user__id', flat=True))
    suggestions = suggestions.exclude(id__in=request.user.friendrequest_sent.values_list('to_user__id', flat=True))

    requests_received = models.User.objects.filter(id__in=request.user.friendrequest_received.values_list('from_user__id', flat=True))
    requests_sent = models.User.objects.filter(id__in=request.user.friendrequest_sent.values_list('to_user__id', flat=True))
    
    friends = request.user.friends.all()
    context = {
        'suggestions' : suggestions,
        'friends': friends,
        'requests_received': requests_received,
        'requests_sent': requests_sent,
    }
    return render(request, "friends.html", context)

@require_POST
def accept_request(request, id):
    new_friend = models.User.objects.get(id=id)
    request.user.friends.add(new_friend)
    request.user.friendrequest_received.get(from_user=new_friend).delete()
    
    return HttpResponse("Accepted")
    
def send_request(request, id):
    to = models.User.objects.get(id=id)
    request_sent = models.FriendRequest(from_user=request.user, to_user=to)
    request_sent.save()
    return HttpResponse("<a class='m-2 bg-black/40 text-black rounded-3xl ml-auto p-2'>Request sent</a>")

def profile_press(request):
    return render(request, "partials/profile-press.html")

def profile(request, username):
    user = get_object_or_404(models.User, username=username)
    feeds = models.Feed.objects.filter(author=user)
    return render(request, "profile.html", {'user' : user, 'feeds': feeds})

def settings(request):
    return render(request, "settings.html")

def edit_profile(request):

    countries = []    

    try:
        response = requests.get("https://countriesnow.space/api/v0.1/countries/iso", timeout=5)
        response.raise_for_status()
        payload = response.json()

        if not payload.get("error"):
            countries = sorted(
                [
                    {"code" : item['Iso2'], "name": item["name"]}
                    for item in payload.get("data", [])
                ],
                key=lambda x: x["name"]
            )
    except requests.RequestException:
        countries = []

    context = {
        "countries" : countries,
        "user_country" : getattr(request.user, "country", ""),
    }
    
    if request.method == "POST":        
        user = request.user
        if "profile_image" in request.FILES:
            user.profile_pic = request.FILES['profile_image']
            user.save()
            return redirect('admin_app:settings')
    return render(request, "edit-profile.html", context)