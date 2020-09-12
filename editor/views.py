from django.shortcuts import render


def home(request):
    context = {
        "title": "coding section"
    }
    return render(request, "editor/index.html", context)

