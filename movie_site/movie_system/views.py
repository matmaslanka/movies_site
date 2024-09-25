from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.text import slugify


from .forms import CustomUserCreationForm, ReviewForm, AddMovieForm, AddGenreForm, AddDirectorForm
# CustomUserCreationForm - registration
from .models import Movies
from .filters import MoviesFilter

# Create your views here.


def register_view(request):     # registration
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, "movie_system/register.html", {
        'form': form
    })


def login_view(request):
    if request.method == "POST":
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            login(request, login_form.get_user())
            return redirect('home')
    else:
        login_form = AuthenticationForm()
    return render(request, "movie_system/login.html", {
        'login_form': login_form
    })


def add_movie_view(request):
    if request.method == "POST":
        add_movie_form = AddMovieForm(data=request.POST, files=request.FILES)
        if add_movie_form.is_valid():
            movie = add_movie_form.save(commit=False)
            movie.slug = slugify(movie.title)
            movie.save()
            return redirect('home')
    else:
        add_movie_form = AddMovieForm()
    return render(request, "movie_system/add-movie.html", {
        'add_movie_form': add_movie_form
    })


def add_genre_view(request):
    if request.method == "POST":
        add_genre_form = AddGenreForm(data=request.POST)
        if add_genre_form.is_valid():
            genre = add_genre_form.save(commit=False)
            genre.slug = slugify(genre.name)
            genre.save()
            return redirect('add-movie')
    else:
        add_genre_form = AddGenreForm()
    return render(request, 'movie_system/add-genre.html', {
        'add_genre_form': add_genre_form
    })


def add_director_view(request):
    if request.method == "POST":
        add_director_form = AddDirectorForm(data=request.POST)
        if add_director_form.is_valid():
            director = add_director_form.save(commit=False)
            director.slug = slugify(director.name)
            director.save()
            return redirect('add-movie')
    else:
        add_director_form = AddDirectorForm()
    return render(request, 'movie_system/add-director.html', {
        'add_director_form': add_director_form
    })


def logout_view(request):
    logout(request)
    return redirect('home')


def index(request):
    sort_by = request.GET.get('sort', 'title')  # Default sorting by 'name'
    allowed_sort_fields = ['title', 'release_date', 'director', '-title', '-release_date', '-director']

    if sort_by in allowed_sort_fields:
        movie_filter = MoviesFilter(request.GET, queryset=Movies.objects.all().order_by(sort_by))
        # If I want to filter, instead movies = Movies.objects.all() I use this line
    else:
        movie_filter = MoviesFilter(request.GET, queryset=Movies.objects.all())

    return render(request, 'movie_system/index.html', {
        'filter': movie_filter.form,
        'movies': movie_filter.qs,
        'sort_by': sort_by
    })


def movie_details(request, movie_slug):
    movie = Movies.objects.get(slug=movie_slug)
    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.movie = movie    # Add movie and user to data
            review.user = request.user
            review_form.save()
            return redirect('movie-detail', movie.slug)
    else:
        review_form = ReviewForm
    return render(request, 'movie_system/movie-details.html', {
        'movie': movie,
        'review_form': review_form,
        'reviews': movie.reviews.all().order_by("-id")
    })
