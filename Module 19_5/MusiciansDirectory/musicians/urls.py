from django.urls import path
from . import views
# from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    # path('register/', views.register, name='register'),
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    # path('login/', views.user_login, name='login'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    # path('logout/', views.logout_user, name='logout'),
    # path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),

    path('', views.musician_list, name="musician_list"),
    # path('add/', views.add_musician, name="add_musician"),
    path('add/', views.AddMusicianView.as_view(), name="add_musician"),
    # path('edit/<int:musician_id>/', views.edit_musician, name="edit_musician"),
    path('edit/<int:musician_id>/', views.EditMusicianView.as_view(), name="edit_musician"),
]
