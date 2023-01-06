from django.urls import path
from movie_app.views import DirectorListCreateAPIView, DirectorDetailUpdateDeleteAPIView
from movie_app.views import MovieListCreateAPIView, MovieDetailUpdateDeleteAPIView, MovieReviewListAPIView
from movie_app.views import ReviewListCreateAPIView, ReviewDetailUpdateDeleteAPIView

urlpatterns = [
    path('directors/', DirectorListCreateAPIView.as_view()),
    path('directors/<int:id>/', DirectorDetailUpdateDeleteAPIView.as_view()),
    path('movies/', MovieListCreateAPIView.as_view()),
    path('movies/<int:id>/', MovieDetailUpdateDeleteAPIView.as_view()),
    path('reviews/', ReviewListCreateAPIView.as_view()),
    path('reviews/<int:id>/', ReviewDetailUpdateDeleteAPIView.as_view()),
    path('movies/reviews/', MovieReviewListAPIView.as_view()),

]
