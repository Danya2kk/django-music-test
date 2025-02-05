# Generated by Django 5.0.6 on 2024-07-02 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_album_cover_image_artist_image_song_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='bio',
            field=models.TextField(verbose_name='Биография'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='artists/', verbose_name='Фото артиста'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Имя исполнителя'),
        ),
    ]
