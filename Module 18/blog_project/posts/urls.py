from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_post, name='addPost'),
    # path('edit/<int:pk>/', views.edit_post, name='editPost'),
    path('edit/<int:id>/', views.edit_post, name='editPost'),
    path('delete/<int:id>/', views.delete_post, name='deletePost'),
]
