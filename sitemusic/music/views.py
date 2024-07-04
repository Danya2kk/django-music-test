from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import AddArtistForm, AddAlbumForm, AddSongForm, PlaylistForm, UserRegistrationForm, UserLoginForm
from .models import Artist, Album, Song, Playlist
# Create your views here.

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Список артистов', 'url_name': 'artists'},
    {'title': 'Доступные альбомы', 'url_name': 'albums'},
]

auth_menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Список артистов', 'url_name': 'artists'},
    {'title': 'Доступные альбомы', 'url_name': 'albums'},
    {'title': 'Добавить артиста', 'url_name': 'add_artist'},
    {'title': 'Добавить альбом артиста', 'url_name': 'add_album'},
    {'title': 'Добавить песню', 'url_name': 'add_song'},
    {'title': 'Список плейлистов', 'url_name': 'playlist_list'},
]


def about(request):
    data = {
        'menu': menu,

    }
    return render(request, 'music/about.html', context=data)


def index(request):
    songs = Song.objects.all()

    data = {
        'title': 'Список всех песен',
        'menu': menu,
        'songs': songs,
        'auth_menu': auth_menu,
    }
    return render(request, 'music/index.html', context=data)


@login_required
def add_song(request):
    if request.method == 'POST':
        form = AddSongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = AddSongForm()

    data = {
        'menu': menu,
        'form': form,
    }

    return render(request, 'music/addsong.html', context=data)


@login_required
def add_album(request):
    if request.method == 'POST':
        form = AddAlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('albums')

    else:
        form = AddAlbumForm()

    data = {
        'menu': menu,
        'form': form,
    }

    return render(request, 'music/addalbum.html', context=data)


@login_required
def add_artist(request):
    if request.method == 'POST':
        form = AddArtistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('artists')
            # try:
            #     Artist.objects.create(**form.cleaned_data)
            #
            # except:
            #     form.add_error(None, 'Ошибка добавления артиста')
    else:
        form = AddArtistForm()

    data = {
        'menu': menu,
        'form': form,
    }

    return render(request, 'music/addartist.html', context=data)


def album_list(request):
    albums = Album.objects.all()
    data = {
        'albums': albums,
    }

    return render(request, 'music/album_list.html', context=data)


def show_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    album_songs = Song.objects.filter(album_id=album_id)
    data = {
        'title': album.title,
        'menu': menu,
        'album': album,
        'albumsongs': album_songs
    }
    return render(request, 'music/album_detail.html', data)


def show_artist(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    artist_songs = Song.objects.filter(artist_id=artist_id)
    data = {
        'name': artist.name,
        'menu': menu,
        'artist': artist,
        'artistsongs': artist_songs
    }
    return render(request, 'music/artist_detail.html', data)


def artist_list(request):
    artists = Artist.objects.all()
    song = get_object_or_404(Song, id=1)
    data = {
        'artists': artists,
        'songs': song,
    }

    return render(request, 'music/artist_list.html', context=data)


@login_required
def playlist_list(request):
    playlists = Playlist.objects.filter(user=request.user)
    data = {
        'menu': menu,
        'playlists': playlists,
    }
    return render(request, 'music/playlist_list.html', context=data)


@login_required
def playlist_detail(request, pk):
    playlist = get_object_or_404(Playlist, pk=pk, user=request.user)
    return render(request, 'music/playlist_detail.html', {'playlist': playlist})


@login_required
def playlist_create(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.user = request.user
            playlist.save()
            form.save_m2m()
            return redirect('playlist_list')
    else:
        form = PlaylistForm()
    return render(request, 'music/playlist_form.html', {'form': form})


@login_required
def playlist_edit(request, pk):
    playlist = get_object_or_404(Playlist, pk=pk, user=request.user)
    if request.method == 'POST':
        form = PlaylistForm(request.POST, instance=playlist)
        if form.is_valid():
            form.save()
            return redirect('playlist_detail', pk=playlist.pk)
    else:
        form = PlaylistForm(instance=playlist)
    return render(request, 'music/playlist_form.html', {'form': form})


@login_required
def playlist_delete(request, pk):
    playlist = get_object_or_404(Playlist, pk=pk, user=request.user)
    if request.method == 'POST':
        playlist.delete()
        return redirect('playlist_list')
    return render(request, 'music/playlist_confirm_delete.html', {'playlist': playlist})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'auth/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'auth/login.html', {'form': form})


@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return render(request, 'auth/logout.html')
