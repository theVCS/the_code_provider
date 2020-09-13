from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Profile


# Create your views here.
@login_required
def profile_view(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    friends_list = profile.friends.all()
    context = {'profile': profile, 'title': 'Profile', friends_list: 'friends_list'}
    return render(request, 'profiles/profile.html', context)
