from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('list', views.DoctorViewSet, basename='doctors')
router.register('specialization', views.SpecializationViewSet, basename='specializations')
router.register('designation', views.DesignationViewSet, basename='designations')
router.register('available_time', views.AvailableTimeViewSet, basename='available_times')
router.register('review', views.ReviewViewSet, basename='reviews')

urlpatterns = [
    path('', include(router.urls)),
]
