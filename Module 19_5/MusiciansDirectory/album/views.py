from django.shortcuts import render, redirect
from . import forms
from . import models
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from django.urls import reverse_lazy

from django.contrib.auth.mixins import UserPassesTestMixin



# Create your views here.


def album_list(request):
    albums = models.Album.objects.all()
    print(albums)
    # print(len(albums))
    albumLength = len(albums)
    # print(albumLength)

    # for album in albums:
    #     print(f"Album: {album.album_name}, Musician: {album.musician.first_name}")

    # if request.GET.get('sort') == 'asc':
    #     albums = albums.order_by('release_date')
    # elif request.GET.get('sort') == 'desc':
    #     albums = albums.order_by('-release_date')

    # sort_param = request.GET.get('sort')
    # if sort_param == 'asc':
    #     albums = albums.order_by('release_date')
    # elif sort_param == 'desc':
    #     albums = albums.order_by('-release_date')
    # elif sort_param == 'asc_rating':
    #     albums = albums.order_by('rating')
    # elif sort_param == 'desc_rating':
    #     albums = albums.order_by('-rating')

    sort_order = request.GET.get('sort_order')
    sort_field = request.GET.get('sort_field')

    if sort_order not in ['asc', 'desc']:
        sort_order = 'asc'

    if sort_field not in ['release_date', 'rating', 'album_name', 'id']:
        sort_field = 'release_date'

    if sort_order == 'asc':
        ordering = sort_field
    else:
        ordering = f'-{sort_field}'

    albums = albums.order_by(ordering)

    # Include the list in the context dictionary
    sort_field_options = {'release_date': 'Release Date',
                          'rating': 'Rating', 'album_name': 'Album Name', 'id': 'ID'}

    # for field, label in sort_field_options.items():
    #     print(field,'-',label)

    search_form = forms.SearchForm(request.GET)
    if search_form.is_valid():
        query = search_form.cleaned_data['query']
        # if query:
        #     albums = albums.filter(album_name__icontains=query)

        if query:
            albums = albums.filter(
                Q(album_name__icontains=query) |
                Q(musician__first_name__icontains=query) |
                Q(musician__last_name__icontains=query) |
                Q(rating__icontains=query)
            )

    # Pagination
    paginator = Paginator(albums, 5)  # Show 5 albums per page

    page = request.GET.get('page')
    try:
        albums = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        albums = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page.
        albums = paginator.page(paginator.num_pages)

    return render(request, 'album_list.html', {'albums': albums, 'albumLength': albumLength, 'sort_field_options': sort_field_options, 'search_form': search_form})


def add_album(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            album_form = forms.AlbumForm(request.POST)
            if album_form.is_valid():
                album_form.save()
                return redirect('add_album')
        else:
            album_form = forms.AlbumForm()
        return render(request, 'add_album.html', {'form': album_form})
    else:
        return redirect('login')


class AddAlbumCreateView(UserPassesTestMixin,CreateView):
    model = models.Album
    template_name = 'add_album.html'
    form_class = forms.AlbumForm
    # success_url = reverse_lazy('home')
    success_url = reverse_lazy('profile')

    def test_func(self):
        # Check if the user is authenticated
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        # Redirect to the login page if the user is not authenticated
        return redirect('login')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def edit_album(request, album_id):
    if request.user.is_authenticated:
        album = models.Album.objects.get(pk=album_id)

        if request.method == 'POST':
            album_form = forms.AlbumForm(request.POST, instance=album)
            if album_form.is_valid():
                album_form.save()
                return redirect('home')
        else:
            album_form = forms.AlbumForm(instance=album)

        return render(request, 'add_album.html', {'form': album_form})
    else:
        return redirect('login')


class EditAlbumUpdateView(UserPassesTestMixin,UpdateView):
    model = models.Album
    template_name = 'add_album.html'
    form_class = forms.AlbumForm
    # success_url = reverse_lazy('home')
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'album_id'

    def test_func(self):
        # Check if the user is authenticated
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        # Redirect to the login page if the user is not authenticated
        return redirect('login')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def delete_album(request, album_id):
    album = models.Album.objects.get(pk=album_id)
    album.delete()
    return redirect('home')


class DeleteAlbumView(DeleteView):
    model = models.Album
    template_name = 'delete_album.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'album_id'
