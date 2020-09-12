from django.shortcuts import render


def home(request):
    params = {
        "title": "coding section"
    }
    return render(request, "editor/index.html", params)

