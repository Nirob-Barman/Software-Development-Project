from django.shortcuts import render, redirect
from . import forms
from . import models
# from posts.models import Post
# from .models import Post


# Create your views here.
def add_post(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('addPost')
    else:
        post_form = forms.PostForm()
    return render(request, 'addPost.html', {'form': post_form})


def edit_post(request, id):
    # post = Post.objects.get(pk=id)
    post = models.Post.objects.get(pk=id)
    # print(post.title)
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            # return redirect('addPost')
            return redirect('homePage')
    else:
        post_form = forms.PostForm(instance=post)
    return render(request, 'addPost.html', {'form': post_form})

def delete_post(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homePage')