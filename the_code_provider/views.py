from django.shortcuts import render
from django.http import HttpResponse


def home(req):
    params = {
        "title": "home"
    }
    return render(req, 'the_code_provider/index.html', params)


def code_editor(req):
    params = {
        "title": "code editor"
    }
    return render(req, 'the_code_provider/code_editor.html', params)
