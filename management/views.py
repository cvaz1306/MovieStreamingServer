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
    # Retrieve the movie object from the database
    movie = get_object_or_404(Movie, pk=movie_id)
    
    # Delete the movie object from the database
    movie.delete()
    
    # Delete the associated thumbnail file from storage
    thumbnail_path = movie.thumbnail.path
    if os.path.exists(thumbnail_path):
        os.remove(thumbnail_path)
    
    # Redirect to a success page or a relevant URL
    return redirect('management')  # Replace 'success_page' with the appropriate URL name
