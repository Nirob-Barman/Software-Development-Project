from typing import Any
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.utils.decorators import method_decorator
# from posts.models import Post
# from .models import Post
from posts.models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

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

# add post using class based view
@method_decorator(login_required, name='dispatch')
class AddPostCreateView(CreateView):
    model = Post
    template_name = 'addPost.html'
    form_class = forms.PostForm
    success_url = reverse_lazy('addPost')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

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

# edit post using class based view


@method_decorator(login_required, name='dispatch')
class EditPostUpdateView(UpdateView):
    model = Post
    template_name = 'addPost.html'
    form_class = forms.PostForm
    # success_url = reverse_lazy('homePage')
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required
def delete_post(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homePage')


# delete post using class based view
@method_decorator(login_required, name='dispatch')
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete.html'
    # success_url = reverse_lazy('homePage')
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'


class DetaiPostsView(DetailView):
    model = Post
    template_name = 'post_details.html'
    # pk_url_kwarg = 'id'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(request.POST)
        # post = self.object
        post = self.get_object()
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.save()
        return self.get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        
        
        context['comment_form'] = comment_form
        context['comments'] = comments
        return context