from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from where_to_go import views


urlpatterns = [
    path('', views.show_index, name='index'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
