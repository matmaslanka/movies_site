from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add-movie', views.add_movie_view, name='add-movie'),
    path('add-genre', views.add_genre_view, name='add-genre'),
    path('add-director', views.add_director_view, name='add-director'),
    path('users/register', views.register_view, name='register'),
    path('users/login', views.login_view, name='login'),
    path('users/logout', views.logout_view, name='logout'),
    path('<slug:movie_slug>', views.movie_details, name='movie-detail'),
]
