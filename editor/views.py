from django.shortcuts import render
from django.http import HttpResponse
import json
from . import drive, question_fetcher
from .models import Coder


def home(request):
    context = {
        "title": "coding section"
    }
    return render(request, "editor/index.html", context)


def submit(request):
    username = request.POST.get("username")
    code = request.POST.get("code")
    file_name = request.POST.get("file_name")
    website = request.POST.get("website")
    preference = request.POST.get("filter")
    language = request.POST.get("language")
    language = language.strip()
    coder = Coder(user_name=username, website=website, code_title=file_name, preference=preference)
    coder.save()
    drive.upload(file_name, code, website, language)
    return HttpResponse(json.dumps(code))


def fetch_question(request):
    url = request.POST.get("url")
    data = question_fetcher.codeforces(url)
    return HttpResponse(data)
