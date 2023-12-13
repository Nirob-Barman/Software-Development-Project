from django.urls import path
from . import views

urlpatterns = [
    # path('add/', views.add_post, name='addPost'),
    path('add/', views.AddPostCreateView.as_view(), name='addPost'),
    # path('edit/<int:pk>/', views.edit_post, name='editPost'),
    
    # path('edit/<int:id>/', views.edit_post, name='editPost'),
    path('edit/<int:id>/', views.EditPostUpdateView.as_view(), name='editPost'),
    # path('delete/<int:id>/', views.delete_post, name='deletePost'),
    path('delete/<int:id>/', views.DeletePostView.as_view(), name='deletePost'),
    # path('details/<int:id>/', views.DetaiPostsView.as_view(), name='detail_post'),
    path('details/<int:pk>/', views.DetaiPostsView.as_view(), name='detail_post'),
]
