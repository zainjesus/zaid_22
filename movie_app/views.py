from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.models import Movie, Review, Director
from movie_app.serialaizers import MovieSerializer, ReviewSerializer, DirectorSerializer


@api_view(['GET'])
def director_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()

        serializer = DirectorSerializer(directors, many=True)

        return Response(data=serializer.data)


@api_view(['GET'])
def director_detail_view(request, **kwargs):
    if request.method == 'GET':
        director = Director.objects.get(id=kwargs['id'])

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
        movie = Movie.objects.get(id=kwargs['id'])

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
        review = Review.objects.get(id=kwargs['id'])

        serializer = ReviewSerializer(review, many=False)

        return Response(data=serializer.data)





