from rest_framework.response import Response
from movie_app.models import Movie, Review, Director
from movie_app.serialaizers import MovieSerializer, ReviewSerializer, DirectorSerializer, MovieReviewSerializer
from movie_app.serialaizers import DirectorCreateSerializer, DirectorUpdateSerializer
from movie_app.serialaizers import MovieCreateSerializer, MovieUpdateSerializer, ReviewValidateSerializer
from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination


class DirectorListCreateAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    validate_serializer_class = DirectorCreateSerializer
    pagination_class = PageNumberPagination

    def post(self, request, *args, **kwargs):
        serializer = self.validate_serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data.get('name')

        directors = Director.objects.create(name=name)
        directors.save()

        return Response(data={'message': "Data received!",
                              "director": self.get_serializer(directors).data},
                        status=status.HTTP_201_CREATED)


class DirectorDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    validate_serializer_class = DirectorUpdateSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        try:
            director = Director.objects.get(id=kwargs['id'])
        except Director.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={'message': 'Director not found!'})

        serializer = self.validate_serializer_class(data=request.data,
                                                    context={'id': director.id})
        serializer.is_valid(raise_exception=True)

        director.name = serializer.validated_data.get('name')
        director.save()

        return Response(data={'message': "Data received!",
                              "director": self.get_serializer(director).data},
                        status=status.HTTP_201_CREATED)


class MovieListCreateAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    validate_serializer_class = MovieCreateSerializer
    pagination_class = PageNumberPagination

    def post(self, request, *args, **kwargs):
        serializer = self.validate_serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        duration = serializer.validated_data.get('duration')
        director = serializer.validated_data.get('director')

        movies = Movie.objects.create(title=title, description=description, duration=duration, director_id=director)
        movies.save()

        return Response(data={'message': "Data received!",
                              "movie": self.get_serializer(movies).data},
                        status=status.HTTP_201_CREATED)


class MovieDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    validate_serializer_class = MovieUpdateSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        try:
            movie = Movie.objects.get(id=kwargs['id'])
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={'message': 'Movie not found!'})

        serializer = self.validate_serializer_class(data=request.data,
                                                    context={'id': movie.id})
        serializer.is_valid(raise_exception=True)

        movie.title = serializer.validated_data.get('title')
        movie.description = serializer.validated_data.get('description')
        movie.duration = serializer.validated_data.get('duration')
        movie.director_id = serializer.validated_data.get('director')
        movie.save()

        return Response(data={'message': 'Data received!',
                              "movie": self.get_serializer(movie).data},
                        status=status.HTTP_201_CREATED)


class ReviewListCreateAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    validate_serializer_class = ReviewValidateSerializer
    pagination_class = PageNumberPagination

    def post(self, request, *args, **kwargs):
        serializer = self.validate_serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        text = serializer.validated_data.get('text')
        movie = serializer.validated_data.get('movie')
        stars = serializer.validated_data.get('stars')

        reviews = Review.objects.create(text=text, movie_id=movie, stars=stars)
        reviews.save()

        return Response(data={'message': "Data received!",
                              "review": self.get_serializer(reviews).data},
                        status=status.HTTP_201_CREATED)


class ReviewDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    validate_serializer_class = ReviewValidateSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        try:
            review = Review.objects.get(id=kwargs['id'])
        except Review.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={'message': 'Review not found!'})

        serializer = self.validate_serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        review.text = serializer.validated_data.get('text')
        review.movie_id = serializer.validated_data.get('movie')
        review.stars = serializer.validated_data.get('stars')
        review.save()

        return Response(data={'message': "Data received!",
                              "review": self.get_serializer(review).data},
                        status=status.HTTP_201_CREATED)


class MovieReviewListAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieReviewSerializer
    pagination_class = PageNumberPagination





