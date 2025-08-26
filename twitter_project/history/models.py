from django.db import models
from django.conf import settings

class History(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    method = models.CharField(max_length=100)
    tweet = models.ForeignKey('tweets.Tweet', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    summary = models.TextField()

    def __str__(self):
        return f'{self.summary}'