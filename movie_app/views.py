from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.models import Movie, Review, Director
from movie_app.serialaizers import MovieSerializer, ReviewSerializer, DirectorSerializer, MovieReviewSerializer
from rest_framework import status


@api_view(['GET', 'POST'])
def director_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()

        serializer = DirectorSerializer(directors, many=True)

        return Response(data=serializer.data)

    elif request.method == 'POST':
        name = request.data.get('name')

        directors = Director.objects.create(name=name)
        directors.save()

        return Response(data={'message': "Data received!",
                              "director": DirectorSerializer(directors).data},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_view(request, **kwargs):
    try:
        directors = Director.objects.get(id=kwargs['id'])
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Director not found!'})

    if request.method == 'GET':
        serializer = DirectorSerializer(directors, many=False)

        return Response(data=serializer.data)

    elif request.method == 'DELETE':
        directors.delete()

        return Response(status=status.HTTP_204_NO_CONTENT,
                        data={'message': 'Data deleted!'})

    else:
        directors.name = request.data.get('name')
        directors.save()

        return Response(data={'message': "Data received!",
                              "director": DirectorSerializer(directors).data},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def movie_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()

        serializer = MovieSerializer(movies, many=True)

        return Response(data=serializer.data)

    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director = request.data.get('director')

        movies = Movie.objects.create(title=title, description=description, duration=duration, director_id=director)
        movies.save()

        return Response(data={'message': "Data received!",
                              "movie": MovieSerializer(movies).data},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_view(request, **kwargs):
    try:
        movies = Movie.objects.get(id=kwargs['id'])
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Movie not found!'})

    if request.method == 'GET':
        serializer = MovieSerializer(movies, many=False)

        return Response(data=serializer.data)

    elif request.method == 'DELETE':
        movies.delete()

        return Response(status=status.HTTP_204_NO_CONTENT,
                        data={'message': 'Data deleted!'})

    else:
        movies.title = request.data.get('title')
        movies.description = request.data.get('description')
        movies.duration = request.data.get('duration')
        movies.director_id = request.data.get('director')
        movies.save()

        return Response(data={'message': 'Data received!',
                              "movie": MovieSerializer(movies).data},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def review_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()

        serializer = ReviewSerializer(reviews, many=True)

        return Response(data=serializer.data)

    elif request.method == 'POST':
        text = request.data.get('text')
        movie = request.data.get('movie')
        stars = request.data.get('stars')

        reviews = Review.objects.create(text=text, movie_id=movie, stars=stars)
        reviews.save()

        return Response(data={'message': "Data received!",
                              "review": ReviewSerializer(reviews).data},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_view(request, **kwargs):
    try:
        reviews = Review.objects.get(id=kwargs['id'])
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Review not found!'})

    if request.method == 'GET':
        serializer = ReviewSerializer(reviews, many=False)

        return Response(data=serializer.data)

    elif request.method == 'DELETE':
        reviews.delete()

        return Response(status=status.HTTP_204_NO_CONTENT,
                        data={'message': 'Data deleted!'})

    else:
        reviews.text = request.data.get('text')
        reviews.movie_id = request.data.get('movie')
        reviews.stars = request.data.get('stars')
        reviews.save()

        return Response(data={'message': "Data received!",
                              "review": ReviewSerializer(reviews).data},
                        status=status.HTTP_201_CREATED)


@api_view(['GET'])
def movies_reviews_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()

        serializer = MovieReviewSerializer(movies, many=True)

        return Response(data=serializer.data)





