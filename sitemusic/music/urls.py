from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path('artists/', views.artist_list, name='artists'),
    path('about/', views.about, name='about'),
    path('artist/<int:artist_id>', views.show_artist, name='artist'),
    path('albums/', views.album_list, name='albums'),
    path('album/<int:album_id>', views.show_album, name='album'),
    path('addartist/', views.add_artist, name='add_artist'),
    path('addalbum/', views.add_album, name='add_album'),
    path('addsong/', views.add_song, name='add_song'),
    path('playlists/', views.playlist_list, name='playlist_list'),
    path('playlists/<int:pk>/', views.playlist_detail, name='playlist_detail'),
    path('playlists/create/', views.playlist_create, name='playlist_create'),
    path('playlists/<int:pk>/edit/', views.playlist_edit, name='playlist_edit'),
    path('playlists/<int:pk>/delete/', views.playlist_delete, name='playlist_delete'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]

