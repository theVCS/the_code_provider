from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {
        "title": "home"
    }
    return render(request, 'the_code_provider/index.html', context)
