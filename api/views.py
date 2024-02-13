from django.http import JsonResponse
from django.shortcuts import render

from management.models import Movie
from django.conf import settings
from django.http import HttpResponse, FileResponse
from django.shortcuts import get_object_or_404
from django.views.generic import View
import os


def DownloadFile(request, file_name):
    # Assuming the file is stored directly in the media root
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)
    print(file_path)
    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        #response.status_code = 206
        return response
    else:
        return HttpResponse("File not found", status=404)

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
