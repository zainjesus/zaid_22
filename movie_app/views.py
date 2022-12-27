from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.models import Movie, Review, Director
from movie_app.serialaizers import MovieSerializer, ReviewSerializer, DirectorSerializer, MovieReviewSerializer
from movie_app.serialaizers import DirectorValidateSerializer, MovieValidateSerializer, ReviewValidateSerializer
from rest_framework import status


@api_view(['GET', 'POST'])
def director_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()

        serializer = DirectorSerializer(directors, many=True)

        return Response(data=serializer.data)

    elif request.method == 'POST':
        serializer = DirectorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data.get('name')

        directors = Director.objects.create(name=name)
        directors.save()

        return Response(data={'message': "Data received!",
                              "director": DirectorSerializer(directors).data},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_view(request, **kwargs):
    try:
        director = Director.objects.get(id=kwargs['id'])
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Director not found!'})

    if request.method == 'GET':
        serializer = DirectorSerializer(director, many=False)

        return Response(data=serializer.data)

    elif request.method == 'DELETE':
        director.delete()

        return Response(status=status.HTTP_204_NO_CONTENT,
                        data={'message': 'Data deleted!'})

    else:
        serializer = DirectorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        director.name = serializer.validated_data.get('name')
        director.save()

        return Response(data={'message': "Data received!",
                              "director": DirectorSerializer(director).data},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def movie_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()

        serializer = MovieSerializer(movies, many=True)

        return Response(data=serializer.data)

    elif request.method == 'POST':
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        duration = serializer.validated_data.get('duration')
        director = serializer.validated_data.get('director')

        movies = Movie.objects.create(title=title, description=description, duration=duration, director_id=director)
        movies.save()

        return Response(data={'message': "Data received!",
                              "movie": MovieSerializer(movies).data},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_view(request, **kwargs):
    try:
        movie = Movie.objects.get(id=kwargs['id'])
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Movie not found!'})

    if request.method == 'GET':
        serializer = MovieSerializer(movie, many=False)

        return Response(data=serializer.data)

    elif request.method == 'DELETE':
        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT,
                        data={'message': 'Data deleted!'})

    else:
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        movie.title = serializer.validated_data.get('title')
        movie.description = serializer.validated_data.get('description')
        movie.duration = serializer.validated_data.get('duration')
        movie.director_id = serializer.validated_data.get('director')
        movie.save()

        return Response(data={'message': 'Data received!',
                              "movie": MovieSerializer(movie).data},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def review_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()

        serializer = ReviewSerializer(reviews, many=True)

        return Response(data=serializer.data)

    elif request.method == 'POST':
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        text = serializer.validated_data.get('text')
        movie = serializer.validated_data.get('movie')
        stars = serializer.validated_data.get('stars')

        reviews = Review.objects.create(text=text, movie_id=movie, stars=stars)
        reviews.save()

        return Response(data={'message': "Data received!",
                              "review": ReviewSerializer(reviews).data},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_view(request, **kwargs):
    try:
        review = Review.objects.get(id=kwargs['id'])
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Review not found!'})

    if request.method == 'GET':
        serializer = ReviewSerializer(review, many=False)

        return Response(data=serializer.data)

    elif request.method == 'DELETE':
        review.delete()

        return Response(status=status.HTTP_204_NO_CONTENT,
                        data={'message': 'Data deleted!'})

    else:
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        review.text = serializer.validated_data.get('text')
        review.movie_id = serializer.validated_data.get('movie')
        review.stars = serializer.validated_data.get('stars')
        review.save()

        return Response(data={'message': "Data received!",
                              "review": ReviewSerializer(review).data},
                        status=status.HTTP_201_CREATED)


@api_view(['GET'])
def movies_reviews_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()

        serializer = MovieReviewSerializer(movies, many=True)

        return Response(data=serializer.data)





