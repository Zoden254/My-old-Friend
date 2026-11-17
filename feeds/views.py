from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def react(request, feedID):
    feed = Feed.objects.get(id=feedID)
    reaction, created = Reaction.objects.get_or_create(reactor=request.user, feed=feed)

    if not created:
        reaction.delete()
        feed.is_reacted = False
    else:
        feed.is_reacted = True
    
    feed.reaction_count = feed.reactions.count()
    return render(request, "partials/reaction-button.html", {'feed' : feed})

def post_comment(request, id):
    commenter = request.user
    feed = get_object_or_404(Feed, id=id)
    if request.POST.get("comment") != "":
        comment = Comment.objects.create(commenter=commenter, feed=feed, content=request.POST.get('comment'))
        comment.save()

    if feed.comments.count():
        return HttpResponse(feed.comments.count())
    else:
        return HttpResponse("&nbsp;")

def comments(request, id):
    comments = Comment.objects.filter(feed=Feed.objects.get(id=id))
    return render(request, "partials/comments.html", {'comments' : comments})