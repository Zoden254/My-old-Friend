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
    path('profile/<str:username>/', views.profile, name="profile"),
    path('settings/', views.settings, name="settings"),
    path('edit-profile/', views.edit_profile, name="edit-profile"),
    path('cancel-request/<int:id>/', views.cancel_request, name="cancel-request"),
]   
