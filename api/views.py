from django.shortcuts import render
from rest_framework import generics
from . import serializers
from administration import models
# Create your views here.

class UsersList(generics.ListAPIView):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()

class NotificationsList(generics.ListAPIView):
    serializer_class = serializers.NotificationsSerializer
    queryset = models.Notification.objects.all()