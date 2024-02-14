from django.urls import include, path

from management import views

urlpatterns=[
    path('',views.home,name="management"),
    path('delete/<int:movie_id>/', view=views.delete_movie, name='delete_movie'),
    path('edit/', views.edit_movie, name='edit_movie'),
]