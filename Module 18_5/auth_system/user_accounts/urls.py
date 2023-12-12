from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('profile/',views.profile,name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('password_change/',views.password_change,name='password_change'),
    path('password_change_without_old_password/',views.password_change_without_old_password,name='password_change_without_old_password'),
]