from django.urls import path
from .views import create_tweet_view

urlpatterns = [
    path('create/', create_tweet_view, name='create_tweet'),
]