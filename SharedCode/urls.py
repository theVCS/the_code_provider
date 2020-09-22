from django.urls import path
from . import views

app_name = 'SharedCode'

urlpatterns = [
    path('', views.home, name="shared_home"),
]
