from django.urls import path
from . import views
from administration.views import home

app_name = 'feeds'

urlpatterns = [
    path('', home, name="home"),
    path('react/<int:feedID>/', views.react, name="react"),
    path('post-comment/<int:id>/', views.post_comment, name="post-comment"),
    path('<int:id>/comments/', views.comments, name="comments")
]

