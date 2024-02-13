from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from vid_host import settings
from . import views
urlpatterns=[
    path('list', view=views.movies),
    
]