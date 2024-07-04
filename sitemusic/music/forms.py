from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Song, Artist, Album, Genre, Playlist


class AddArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'bio', 'image']


class AddAlbumForm(forms.ModelForm):
    genre = forms.ModelChoiceField(queryset=Genre.objects.all(), empty_label="Жанр не выбран", label='Жанр')
    artist = forms.ModelChoiceField(queryset=Artist.objects.all(), empty_label='Артист не выбран', label='Артист')

    class Meta:
        model = Album
        fields = '__all__'


class AddSongForm(forms.ModelForm):
    album = forms.ModelChoiceField(queryset=Album.objects.all(), empty_label='Неизвестно', label='Альбом')

    class Meta:
        model = Song
        fields = '__all__'


class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['name', 'songs']
        widgets = {
            'songs': forms.CheckboxSelectMultiple,
        }


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=255)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
