import random
import string

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import json

from django.urls import reverse

from . import drive
# from .models import Code
import uuid
from django.apps import apps
from .forms import UserSearchForm

Profile = apps.get_model('profiles', 'Profile')


def random_string_generator(size=6, chars=string.ascii_lowercase + string.digits + string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))


def home(request):
    if request.method == 'POST':
        user_search_form = UserSearchForm(request.POST)
        if user_search_form.is_valid():
            try:
                user = User.objects.get(username=user_search_form.cleaned_data['username'])
                context = {'username': user}
                return HttpResponseRedirect(reverse('profiles:profile', kwargs=context))
            except User.DoesNotExist:
                user_search_form.add_error('username', ValidationError("User Doesn't Exist"))
        return render(request, "editor/index.html", {'user_search_form': user_search_form})
    else:
        user_search_form = UserSearchForm()
        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
            friends_list = profile.friends.all()
            context = {
                "title": "CodeViewer",
                "friends_list": friends_list,
                "user_search_form": user_search_form
            }
        else:
            context = {
                "title": "home",
                "user_search_form": user_search_form
            }

        # getting data
        file_name = request.GET.get("id")
        language = request.GET.get("language")
        website = request.GET.get("website")
        
        context["code"] = drive.get_content(website, language, file_name)
        context["language"] = language

        return render(request, "userCodes/index.html", context)
