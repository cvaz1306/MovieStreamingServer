from django.shortcuts import render
from random import shuffle
from management.models import Movie
import math

# Create your views here.
def home(request):
    f20m=Movie.objects.all().order_by('?')[:20]
    recommended=Movie.recommend_movies(min(3,Movie.objects.all().count()))
    return render(template_name="home.html",request=request,context={
        'f20movies':f20m,
        'recommended':recommended
    })
def watch(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(template_name="watch.html",request=request, context={
        'movie': movie
    })