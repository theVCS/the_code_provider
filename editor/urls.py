from django.urls import path
from . import views

app_name = 'editor'

urlpatterns = [
    path('', views.home, name="home"),
    path('code/<str:unique_code_id>/', views.get_code_view, name='get_code_view'),
    path('submit/', views.submit, name="submit"),
    path('fetch_question/', views.fetch_question, name="fetch_question"),
    path('share/', views.share, name="share"),
    path('show/', views.show, name="show"),
    path('tempEdit/', views.edit_temp, name="tempEdit"),
    path('send_message/', views.send_message, name="send_message"),
    path('delete_message/', views.delete_message, name="send_message"),
]
