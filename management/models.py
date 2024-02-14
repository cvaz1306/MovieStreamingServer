import os
import random
from django.db import models
# Create your models here.
class Movie(models.Model):
    title=models.TextField()
    movie=models.FileField(upload_to="movies")
    thumbnail=models.ImageField(upload_to="thumbnails", default="https://via.placeholder.com/200")
    ranking=models.FloatField(default=1)
    def delete(self, *args, **kwargs):
        # Delete the associated files from storage when the movie object is deleted
        if self.movie:
            if os.path.exists(self.movie.path):
                os.remove(self.movie.path)
        if self.thumbnail:
            if os.path.exists(self.thumbnail.path):
                os.remove(self.thumbnail.path)
        super().delete(*args, **kwargs)
    @staticmethod
    def recommend_movies(num):
        # Get all movies
        all_movies = Movie.objects.all().order_by('?')
        
        # Add a random number to each movie's ranking
        for movie in all_movies:
            movie.adjusted_ranking = movie.ranking + random.uniform(0, 0.5)  # Adjust this range as needed
        
        # Sort the movies based on adjusted ranking
        sorted_movies = sorted(all_movies, key=lambda x: x.adjusted_ranking, reverse=True)
        
        # Select the top 3 movies
        top_movies = sorted_movies[:num]
        
        return top_movies