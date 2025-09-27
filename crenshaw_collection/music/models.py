from django.db import models


class Album(models.Model):
    cover = models.ImageField(upload_to='album_covers/', blank=True, null=True)
    artist = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return f"{self.artist} - {self.title}"