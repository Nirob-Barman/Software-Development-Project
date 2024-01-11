from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()

# router.register(r'services', views.ServiceViewSet, basename='services')
# router.register(r'', views.ServiceViewSet, basename='services')
router.register('', views.ServiceViewSet, basename='services')

urlpatterns = [
    path('', include(router.urls)),
]
