from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.set_session, name='home'),
    path('get_cookie/', views.get_cookie, name='get_cookie'),
    path('get_session/', views.get_session, name='get_session'),
    path('delete_cookie/', views.delete_cookie, name='delete_cookie'),
    path('delete_session/', views.delete_session, name='delete_session'),
]
