from django.http import HttpResponse
from django.shortcuts import render
from . import drive
import json

# Create your views here.


def home(request):
    unique_id = request.GET.get("id")
    code = drive.show_shared(unique_id)
    context = {
        "title": "sharedCode",
        'code': code,
    }
    return render(request, 'sharedcode/index.html', context)


def show_answer(request):
    unique_id = request.GET.get("id")
    language = request.GET.get("language")
    website = request.GET.get("website")
    code = drive.get_content(website, language, unique_id)

    context = {
        "title": "sharedCode",
        'code': code,
    }

    return render(request, 'sharedcode/index.html', context)