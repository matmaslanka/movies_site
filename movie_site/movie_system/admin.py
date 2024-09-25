from django.contrib import admin

from .models import Movies, Director, Genre, Actor, Watchlist, Review


class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class MoviesAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date')
    prepopulated_fields = {'slug': ('title',)}


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie', 'user', 'review_date')


# Register your models here.
admin.site.register(Movies, MoviesAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Actor)
admin.site.register(Watchlist)
admin.site.register(Review, ReviewAdmin)
