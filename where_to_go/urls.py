from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from places import views


urlpatterns = [
    path('', views.show_index, name='index'),
    path('admin/', admin.site.urls),
    path('places/<int:place_id>/', views.get_json_data),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
