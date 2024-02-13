from watch import views
from django.urls import path
urlpatterns=[
    path('',views.home, name="home"),
    path('watch/<int:movie_id>/',views.watch)
]

