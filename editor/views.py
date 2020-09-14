from django.shortcuts import render
from django.http import HttpResponse
import json
from . import drive


def home(request):
    context = {
        "title": "coding section"
    }

    # site = request.GET.get("site")

    return render(request, "editor/index.html", context)


def submit(request):

    data = request.POST.get("code")
    file_name = request.POST.get("file_name")

    drive.upload(file_name, data)

    return HttpResponse(json.dumps(data))
