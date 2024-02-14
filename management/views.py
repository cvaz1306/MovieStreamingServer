from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import MovieForm


def home(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            print("Saving")
            form.save()
            return redirect('management')
        else:
            print(f"Not saving \n{request.POST}\n{request.FILES}")    
    else:
        form = MovieForm()
    return render(template_name="management.html",request=request,context={
        'movies':Movie.objects.all(),
        'form': form,
    })
def add(request):
    return render(template_name="add.html", request=request, context={})

# views.py

from django.shortcuts import redirect, get_object_or_404
from .models import Movie
import os

def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    
    movie.delete()
    
    thumbnail_path = movie.thumbnail.path
    if os.path.exists(thumbnail_path):
        os.remove(thumbnail_path)
    return redirect('management')  
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm

def edit_movie(request):
    
    
    # Retrieve the movie object or return 404 if not found
    
    
    if request.method == 'GET':
        movie_id=request.GET.get('movie_id',0)
        movie = get_object_or_404(Movie, id=movie_id)
        ranking=float(request.GET.get('ranking',1))
        movie.ranking=float(ranking)
        movie.save()
        return redirect('/management')  # Redirect to management page after successful update
    else:
        return HttpResponse("Incorrect Method")