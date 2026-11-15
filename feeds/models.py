from django.db import models
from administration.models import User
# Create your models here.

class Feed(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feeds")
    picture = models.ImageField(upload_to="static/images/feeds", blank=True, null=True)
    caption = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    scope = models.CharField(choices=[('friends', 'Friends'), ('public', 'Public')])

    def __str__(self):
        return f"{self.author.username}'s Post"

class Reaction(models.Model):
    reactor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reacted_feeds")
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, related_name="reactions")

    def __str__(self):
        return f"{self.reactor} reactions to {self.feed}"
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["reactor", "feed"], name="unique_post_reaction")
        ]
    
class Comment(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, related_name="comments")
    commenter = models.ForeignKey(User,on_delete=models.CASCADE, related_name="comments")
    identification = models.BooleanField(default=True)
    content = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)


class CommentReply(models.Model):
    Comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="replies")
    replier = models.ForeignKey(User, on_delete=models.CASCADE)
    identification = models.BooleanField(default=True)
    content = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)