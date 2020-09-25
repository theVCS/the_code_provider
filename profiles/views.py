from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from .forms import UserSearchForm
from .models import Profile, FriendRequest, Message
from .decorators import user_can_accept_friend_request

Code = apps.get_model('editor', 'Code')


# Create your views here.
@login_required
def profile_view(request, username):

    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    followers_list = profile.followers.all()
    friends_list = profile.friends.all()
    public_codes = Code.objects.filter(user=user, sharing_option='public').order_by('-date')
    private_codes = Code.objects.filter(user=user, sharing_option='private').order_by('-date')
    me_codes = Code.objects.filter(user=user, sharing_option='me').order_by('-date')
    messages = Message.objects.filter(recieved_by=user)
    pending_friend_requests = FriendRequest.objects.filter(status='pending', request_to=user)

    if request.method == 'POST':
        user_search_form = UserSearchForm(request.POST)
        if user_search_form.is_valid():
            try:
                user = User.objects.get(username=user_search_form.cleaned_data['username'])
                context = {'username': user}
                return HttpResponseRedirect(reverse('profiles:profile', kwargs=context))
            except User.DoesNotExist:
                user_search_form.add_error('username', ValidationError("User Doesn't Exist"))
    else:
        user_search_form = UserSearchForm()

    context = {'profile': profile, 'profile_user': user, 'title': 'Profile', 'friends_list': friends_list,
               'pending_friend_requests': pending_friend_requests, 'friends_count': friends_list.count(),
               'followers_list': followers_list, 'public_codes': public_codes, 'private_codes': private_codes,
               'me_codes': me_codes, 'messages': messages, "user_search_form": user_search_form}
    return render(request, 'profiles/profile.html', context)


@login_required
def send_friend_request_view(request, friend_username):
    request_by = request.user
    request_to = User.objects.get(username=friend_username)
    friend_request = FriendRequest.create(request_by=request_by, request_to=request_to)
    friend_request.save()
    return HttpResponseRedirect(reverse('profiles:profile', kwargs={'username': friend_username}))


@login_required
@user_can_accept_friend_request
def accept_friend_request_view(request, friend_request_id):
    friend_request = FriendRequest.objects.get(pk=friend_request_id)
    request_to_profile = Profile.objects.get(user=friend_request.request_to)
    request_by_profile = Profile.objects.get(user=friend_request.request_by)
    request_to_profile.friends.add(friend_request.request_by)
    request_by_profile.friends.add(friend_request.request_to)
    friend_request.delete()
    return HttpResponseRedirect(reverse('profiles:profile', kwargs={'username': request.user.username}))


@login_required
def follow_user(request, user_name):
    user = User.objects.get(username=user_name)
    user_profile = Profile.objects.get(user=user)
    follow_request_user_profile = Profile.objects.get(user=request.user)
    user_profile.followers.add(request.user)
    follow_request_user_profile.following.add(user)
    return HttpResponseRedirect(reverse('profiles:profile', kwargs={'username': user}))
