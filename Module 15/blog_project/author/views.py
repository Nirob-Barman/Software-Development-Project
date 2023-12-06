from django.shortcuts import render, redirect
# from django.urls import reverse
from . import forms


# Create your views here.


def add_author(request):
    if request.method == 'POST':
        author_form = forms.AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            # author_form = forms.AuthorForm()
            # return render(request, 'addAuthor.html', {'form': author_form})
            # redirect('add_author')
            return redirect('add_author')
            # return redirect(reverse('add_author'))
    else:
        author_form = forms.AuthorForm()
    # author_form = forms.AuthorForm()
    return render(request, 'addAuthor.html', {'form': author_form})
