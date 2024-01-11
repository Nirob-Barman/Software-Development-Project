from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register('list', views.PatientViewSet, basename='patients')

urlpatterns = [
    path('', include(router.urls)),
    path('register', views.UserRegistrationView.as_view(), name='register'),
    # path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('active/<uid64>/<token>', views.activate, name='activate'),

]