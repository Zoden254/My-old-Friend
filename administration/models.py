from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='static/images', default='blank_profile.jpg')
    phone = models.CharField(max_length=15, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    friends = models.ManyToManyField('self', symmetrical=True, blank=True)

    def __str__(self):
        return self.username
    
class RelatedField(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    field = models.CharField(max_length=255)
    from_year = models.IntegerField()
    to_year = models.IntegerField()
    country = models.CharField(max_length=40, default='Kenya')
    location = models.CharField(max_length=40)
    institution = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.field


class ReunitedClass(models.Model):
    name = models.CharField(max_length=50)
    members = models.ManyToManyField(User)


class FriendRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('denied', 'Denied')
    ]

    from_user = models.ForeignKey(User, related_name="friendrequest_sent", on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name="friendrequest_received", on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES, max_length=20, default='pending')

    class Meta:
        unique_together = ('from_user', 'to_user')

    def __str__(self):
        return f"From {self.from_user.username} to {self.to_user.username}."

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    content = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.content