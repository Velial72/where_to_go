from django.contrib import admin
from django.urls import path
from where_to_go import views

urlpatterns = [
    path('', views.show_index, name='index'),
    path('admin/', admin.site.urls),
]
