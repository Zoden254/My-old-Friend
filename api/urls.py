from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path('users/', views.UsersList.as_view()),
    path('user/<int:pk>/', views.UserDetails.as_view()),
    path('notifications/', views.NotificationsList.as_view()),
]
