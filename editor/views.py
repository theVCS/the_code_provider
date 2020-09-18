import random
import string
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import json

from django.urls import reverse

from . import drive, question_fetcher
from .models import Code
import uuid
from django.apps import apps

Profile = apps.get_model('profiles', 'Profile')


def random_string_generator(size=6, chars=string.ascii_lowercase + string.digits + string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))


def home(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        friends_list = profile.friends.all()
        context = {
            "title": "coding section",
            "friends_list": friends_list,
        }
    else:
        context = {
            "title": "home",
        }
    return render(request, "editor/index.html", context)


def submit(request):
    code_text = request.POST.get("code")
    # file_name = request.POST.get("file_name")
    website = request.POST.get("website")
    sharing_option = request.POST.get("filter")
    language = request.POST.get("language")
    language = language.strip()
    unique_code_id = random_string_generator()
    while Code.objects.filter(unique_code_id=unique_code_id).count() > 0:
        unique_code_id = random_string_generator()
    code = Code.create(unique_code_id=unique_code_id, user=request.user, website=website, language=language,
                       sharing_option=sharing_option)
    # drive.upload(unique_code_id, code, website, language)

    return HttpResponseRedirect(reverse('editor:get_code_view', kwargs={'unique_code_id': unique_code_id}))


def fetch_question(request):
    url = request.POST.get("url")
    data = question_fetcher.codeforces(url)
    return HttpResponse(data)


def share(request):
    data = request.POST.get("code")
    file_name = uuid.uuid1().hex
    language = request.POST.get("language")
    drive.sharing_code(data, language, file_name)
    return HttpResponse(json.dumps({'file_name': file_name}))


def show(request):
    id = request.GET.get("id")
    code = drive.show_shared(id)
    return HttpResponse(json.dumps({'code': code}))


def edit_temp(request):
    code = request.POST.get('code')
    language = request.POST.get('language')
    language = language.strip()
    file_name = request.POST.get('file_name')
    file_name = drive.temp_edit(code, language, file_name)
    return HttpResponse(json.dumps({'file_name': file_name}))


def get_code_view(request, unique_code_id):
    # get code file with id : unique_code_id
    return HttpResponse("Will be available soon")
