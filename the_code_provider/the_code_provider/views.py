from django.shortcuts import render
from django.http import HttpResponse


def home(req):
    params = {
        "title": "home"
    }
    return render(req, 'index.html', params)


