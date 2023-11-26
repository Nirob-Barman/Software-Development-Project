from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home),
    path("app_name/", include("app_name.urls")),
    path('contact/', views.contact),
]
