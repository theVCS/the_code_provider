from django.contrib import admin
from django.urls import path
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('accounts/', include('accounts.urls')),
    path('code_editor/', include('editor.urls'), name="code_editor"),
    path('profile/', include('profiles.urls')),
    path('shared/', include('SharedCode.urls')),
    path('userCodes/', include('userCodes.urls')),
]
