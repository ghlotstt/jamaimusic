from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
