from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TweetForm
from .models import Tweet

@login_required
def create_tweet_view(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list') # Redirect to a tweet list page
    else:
        form = TweetForm()

    context = {'form': form}
    return render(request, 'tweets/create_tweet.html', context)
