from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.models import Movie, Review, Director
from movie_app.serialaizers import MovieSerializer, ReviewSerializer, DirectorSerializer, MovieReviewSerializer
from rest_framework import status


@api_view(['GET'])
def director_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()

        serializer = DirectorSerializer(directors, many=True)

        return Response(data=serializer.data)


@api_view(['GET'])
def director_detail_view(request, **kwargs):
    if request.method == 'GET':
        try:
            director = Director.objects.get(id=kwargs['id'])
        except Director.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={"message": "Director not found!"})

        serializer = DirectorSerializer(director, many=False)

        return Response(data=serializer.data)


@api_view(['GET'])
def movie_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()

        serializer = MovieSerializer(movies, many=True)

        return Response(data=serializer.data)


@api_view(['GET'])
def movie_detail_view(request, **kwargs):
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(id=kwargs['id'])
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={"message": "Movie not found!"})

        serializer = MovieSerializer(movie, many=False)

        return Response(data=serializer.data)


@api_view(['GET'])
def review_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()

        serializer = ReviewSerializer(reviews, many=True)

        return Response(data=serializer.data)


@api_view(['GET'])
def review_detail_view(request, **kwargs):
    if request.method == 'GET':
        try:
            review = Review.objects.get(id=kwargs['id'])
        except Review.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={"message": "Review not found!"})

        serializer = ReviewSerializer(review, many=False)

        return Response(data=serializer.data)


@api_view(['GET'])
def movies_reviews_view(request):
    if request.method == 'GET':
        movie = Movie.objects.all()

        serializer = MovieReviewSerializer(movie, many=True)

        return Response(data=serializer.data)





