import datetime

from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.name}'


class Director(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    biography = models.TextField(max_length=1000)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.name}'


class Actor(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    biography = models.TextField(max_length=1000)


class Movies(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    release_date = models.DateField()
    duration = models.DurationField()
    rating = models.IntegerField(default=3, validators=[MaxValueValidator(5), MinValueValidator(1)])
    poster_image = models.ImageField(upload_to='images')
    trailer_URL = models.URLField()
    synopsis = models.TextField(max_length=1000)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    director = models.ManyToManyField(Director, blank=True)

    class Meta:
        verbose_name_plural = 'Movies'

    def __str__(self):
        return f'{self.title} ({self.release_date})'


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movies, blank=True)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    review_text = models.TextField(max_length=1000)
    review_date = models.DateField(default=datetime.date.today)
