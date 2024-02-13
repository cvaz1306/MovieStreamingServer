import os
from django.db import models

# Create your models here.
class Movie(models.Model):
    title=models.TextField()
    movie=models.FileField(upload_to="movies")
    thumbnail=models.ImageField(upload_to="thumbnails", default="https://via.placeholder.com/200")
    def delete(self, *args, **kwargs):
        # Delete the associated files from storage when the movie object is deleted
        if self.movie:
            if os.path.exists(self.movie.path):
                os.remove(self.movie.path)
        if self.thumbnail:
            if os.path.exists(self.thumbnail.path):
                os.remove(self.thumbnail.path)
        super().delete(*args, **kwargs)
