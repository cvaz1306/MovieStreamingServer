from django.shortcuts import render

from management.models import Movie

# Create your views here.
def home(request):
    return render(template_name="home.html",request=request,context={
        'movies':Movie.objects.all()
    })
def watch(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(template_name="watch.html",request=request, context={
        'movie': movie
    })