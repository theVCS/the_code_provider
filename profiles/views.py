from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Profile, FriendRequest


# Create your views here.
@login_required
def profile_view(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    friends_list = profile.friends.all()
    pending_friend_requests = FriendRequest.objects.filter(status='pending', request_to=user)
    context = {'profile': profile, 'profile_user': user, 'title': 'Profile', friends_list: 'friends_list',
               'pending_friend_requests': pending_friend_requests}
    return render(request, 'profiles/profile.html', context)


def send_friend_request_view(request, friend_username):
    request_by = request.user
    request_to = User.objects.get(username=friend_username)
    friend_request = FriendRequest.create(request_by=request_by, request_to=request_to)
    friend_request.save()
    return HttpResponseRedirect(reverse('profiles:profile', kwargs={'username': friend_username}))
