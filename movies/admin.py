from django.contrib import admin

from .models import Category, Actor, Genre, Movie, MovieShots, RatingStart, Rating, Reviews

admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(RatingStart)
admin.site.register(Rating)
admin.site.register(Reviews)
