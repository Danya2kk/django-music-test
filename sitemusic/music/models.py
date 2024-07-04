from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=255, )

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя исполнителя')
    bio = models.TextField(verbose_name='Биография')
    image = models.ImageField(upload_to='artists/', verbose_name='Фото артиста')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('artist', kwargs={'artist_id': self.pk})


class Album(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название альбома')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    release_date = models.DateField(verbose_name='Дата релиза')
    cover_image = models.ImageField(upload_to='albums/', verbose_name='Фото альбома')

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Альбом')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name='Артист')
    file = models.FileField(upload_to='songs/', verbose_name='Файл песни')

    def __str__(self):
        return self.title


class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.name
