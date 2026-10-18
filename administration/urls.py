<<<<<<< HEAD
from django.urls import path
from . import views

app_name = "admin_app"

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_view, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout_view, name="logout"),
    path('v-nav', views.v_nav, name="v-nav"),
    path('notification-sync/', views.notification_sync, name='notification-sync'),
    path('notification-box/', views.notification_box, name='not-box'),
    path('friends/', views.friends, name="friends-page"),
    path('accept-request/<int:id>/', views.accept_request, name="accept-request"),
    path('send-request/<int:id>/', views.send_request, name="send-request"),
    path('profile-press/', views.profile_press, name="profile-press"),
]   
=======
from django.urls import path
from . import views

app_name = "admin_app"

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_view, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout_view, name="logout"),
    path('v-nav', views.v_nav, name="v-nav"),
    path('notification-sync/', views.notification_sync, name='notification-sync'),
    path('notification-box/', views.notification_box, name='not-box'),
    path('friends/', views.friends, name="friends-page"),
    path('accept-request/<int:id>/', views.accept_request, name="accept-request"),
    path('send-request/<int:id>/', views.send_request, name="send-request"),
    path('profile-press/', views.profile_press, name="profile-press"),
]   
>>>>>>> d049361272bdd2b52e1c6c1ef2b2363d9a736d19
