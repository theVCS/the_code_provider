from django.shortcuts import render
from django.http import HttpResponse
import json
from . import drive, question_fetcher
from .models import Code
import uuid


def home(request):
    context = {
        "title": "coding section"
    }
    return render(request, "editor/index.html", context)


def submit(request):
    code_text = request.POST.get("code")
    # file_name = request.POST.get("file_name")
    website = request.POST.get("website")
    sharing_option = request.POST.get("filter")
    language = request.POST.get("language")
    language = language.strip()
    code = Code.create(unique_code_id="a", user=request.user, website=website, language=language,
                       sharing_option=sharing_option)
    # drive.upload(file_name, code, website, language)
    return HttpResponse(json.dumps(code_text))


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
