from django.apps import apps
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from profiles.forms import ProfileForm
# Create your views here.
from django.urls import reverse

Profile = apps.get_model('profiles', 'Profile')


def signup(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()
            name = profile_form.cleaned_data['name']
            email_id = profile_form.cleaned_data['email_id']
            profile = Profile.objects.create(user=user, name=name, email_id=email_id)
            profile.save()
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        context = {'user_form': user_form, 'profile_form': profile_form}
        return render(request, 'accounts/signup.html', context)
    else:
        user_form = UserCreationForm()
        profile_form = ProfileForm()
        context = {'user_form': user_form, 'profile_form': profile_form}
        return render(request, 'accounts/signup.html', context)
