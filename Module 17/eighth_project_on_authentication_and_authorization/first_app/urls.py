from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('password_change/', views.password_change, name='password_change'),
    path('password_change_without_old_password/', views.password_change_without_old_password,
         name='password_change_without_old_password'),
    path('change_user_data/', views.change_user_data, name='change_user_data'),
    path('profile/', views.profile, name='profile'),
]
