from django.shortcuts import render
from django.http import HttpResponse
import json
from . import drive, question_fetcher


def home(request):
    context = {
        "title": "coding section"
    }
    return render(request, "editor/index.html", context)


def submit(request):
    data = request.POST.get("code")
    file_name = request.POST.get("file_name")
    drive.upload(file_name, data)
    return HttpResponse(json.dumps(data))


def fetch_question(request):
    url = request.POST.get("url")
    data = question_fetcher.codeforces(url)
    return HttpResponse(data)
