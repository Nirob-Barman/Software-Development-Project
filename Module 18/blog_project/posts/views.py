from django.shortcuts import render, redirect
from . import forms
from . import models
# from posts.models import Post
# from .models import Post
from posts.models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_post(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            # post_form.cleaned_data['author'] = request.user
            post_form.instance.author = request.user
            post_form.save()
            return redirect('addPost')
    else:
        post_form = forms.PostForm()
    return render(request, 'addPost.html', {'form': post_form})


@login_required
def edit_post(request, id):
    # post = Post.objects.get(pk=id)
    post = models.Post.objects.get(pk=id)
    # print(post.title)
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.save()
            # return redirect('addPost')
            return redirect('homePage')
    else:
        post_form = forms.PostForm(instance=post)
    return render(request, 'addPost.html', {'form': post_form})

@login_required
def delete_post(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homePage')
