from django.urls import path
from . import views

app_name = 'editor'

urlpatterns = [
    path('submit/', views.submit, name="home"),
    path('', views.home, name="home"),

]
