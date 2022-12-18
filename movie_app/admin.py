from django.contrib import admin
from movie_app.models import Director, Movie, Review


class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'director')
    list_display_links = ('title',)
    search_fields = ('title', 'director')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie', 'stars')
    list_display_links = ('movie',)


admin.site.register(Director, DirectorAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)
