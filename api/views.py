from django.http import JsonResponse
from django.shortcuts import render

from management.models import Movie

# Create your views here.
def movies(request):
    return JsonResponse([
        {
            "title":m.title,
            "thumbnail":m.thumbnail.url,
            "video":m.movie.url
        } for m in Movie.objects.all()
        ], safe=False
                        )
    