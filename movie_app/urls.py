from django.urls import path
from movie_app.views import director_view, director_detail_view
from movie_app.views import movie_view, movie_detail_view, review_view, review_detail_view


urlpatterns = [
    path('api/v1/directors/', director_view),
    path('api/v1/directors/<int:id>/', director_detail_view),
    path('api/v1/movies/', movie_view),
    path('api/v1/movies/<int:id>/', movie_detail_view),
    path('api/v1/reviews/', review_view),
    path('api/v1/reviews/<int:id>/', review_detail_view)
]
