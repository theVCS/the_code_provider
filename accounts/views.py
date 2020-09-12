from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('code_provider:home'))
    else:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                login(request, user)
                return HttpResponseRedirect(reverse('editor:home'))
            return render(request, 'accounts/signup.html', {'form': form})
        form = UserCreationForm()
        return render(request, 'accounts/signup.html', {'form': form})
