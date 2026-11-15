from django.shortcuts import render
from .models import *

# Create your views here.
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