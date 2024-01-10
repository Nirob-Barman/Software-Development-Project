from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('', views.AppointmentViewSet, basename='appointments')

urlpatterns = [
    path('', include(router.urls)),
]
