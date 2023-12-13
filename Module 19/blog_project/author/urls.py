from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    # path('login/', views.user_login, name='user_login'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    # path('logout/', views.logout_view, name='user_logout'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('profile/edit/password_change/',
         views.password_change, name='password_change'),
]
