from rest_framework import serializers
from administration import models
from administration import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'

class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notification
        fields = '__all__'