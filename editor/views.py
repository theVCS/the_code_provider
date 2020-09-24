import random
import string

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import json

from django.urls import reverse

from . import drive, question_fetcher
from .models import Code
import uuid
from django.apps import apps

Profile = apps.get_model('profiles', 'Profile')
Message = apps.get_model('profiles', 'Message')


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
    website = request.POST.get("website")
    sharing_option = request.POST.get("filter")
    language = request.POST.get("language")
    language = language.strip()
    unique_code_id = random_string_generator()
    problem_title = request.POST.get("problem_title")
    while Code.objects.filter(unique_code_id=unique_code_id).count() > 0:
        unique_code_id = random_string_generator()

    if "codeforces" in problem_title:
        problem_title = problem_title[-1:-7:-1][::-1]

    code = Code.create(unique_code_id=unique_code_id, user=request.user, website=website, language=language,
                       sharing_option=sharing_option, problem_title=problem_title)

    file_name = drive.upload(unique_code_id, code_text, website, language)
    return HttpResponseRedirect(reverse('editor:get_code_view', kwargs={'unique_code_id': unique_code_id}))


def fetch_question(request):
    url = request.POST.get("url")

    problem_title = None

    if "codeforces" in url:
        problem_title = url[-1:-7:-1][::-1]

    data = question_fetcher.codeforces(url)
    data = json.loads(data)

    data['public_codes'] = list(Code.objects.filter(problem_title=problem_title, sharing_option='public').values())

    for code in data['public_codes']:
        del code['date']
        del code['sharing_option']
        del code['id']
        del code['user_id']
        del code['problem_title']

    data = json.dumps(data)

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


def send_message(request):
    message_text = request.POST.get("message_text")
    friend_list = json.loads(request.POST.get("friend_list"))

    for user in friend_list:
        message = Message.create(message_text=message_text,  send_by=request.user, recieved_by=User.objects.get(username=user), link="https://localhost:8000")

    return HttpResponse({"name": "prince"})


def delete_message(request):
    message_id = request.POST.get("id")
    Message.objects.get(id=message_id).delete()
    return HttpResponse({"name": "prince"})
