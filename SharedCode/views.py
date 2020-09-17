from django.http import HttpResponse
from django.shortcuts import render
from . import drive
import json

# Create your views here.


def home(request):
    id = request.GET.get("id")
    code = drive.show_shared(id)
    context = {
        "title": "sharedCode",
        'code': code,
    }
    return render(request, 'sharedcode/index.html', context)
