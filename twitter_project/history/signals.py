from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import History

@receiver(post_save, sender='tweets.Tweet')
def create_history_on_tweet_creation(sender, instance, created, **kwargs):
    if created:
        summary_message = f'User {instance.user.username} Created tweet with a content of "{instance.content}" at {instance.created_at.strftime("%Y-%m-%d %H:%M:%S")}'
        History.objects.create(
            user=instance.user,
            method="POST",
            tweet=instance,
            summary=summary_message,
        )