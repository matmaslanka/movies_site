import django_filters
from .models import Movies


class MoviesFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    director = django_filters.CharFilter(lookup_expr='icontains')
    release_date = django_filters.DateFromToRangeFilter()
    genre = django_filters.CharFilter(lookup_expr='icontains')
    rating = django_filters.NumberFilter(lookup_expr='gte')

    class Meta:
        model = Movies
        fields = ['title', 'director', 'release_date', 'genre', 'rating']
