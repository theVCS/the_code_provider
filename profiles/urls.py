from django.urls import path
from . import views

app_name = 'profiles'
urlpatterns = [
    path('<str:username>/', views.profile_view, name='profile'),
    path('send_friend_request/<str:friend_username>/', views.send_friend_request_view, name='send_friend_request'),
]
