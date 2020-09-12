from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('shop/', include('shop.urls'), name="shopHome"),
    path('blog/', include('blog.urls'), name="blogHome"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
