from rest_framework import serializers
from movie_app.models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = ('id', 'name', 'movies_count')

    def get_movies_count(self, director):
        return director.movies.all().count()


class MovieSerializer(serializers.ModelSerializer):
    director = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration', 'director')

    def get_director(self, movie):
        return movie.director.name


class ReviewSerializer(serializers.ModelSerializer):
    movie = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ('id', 'text', 'stars', 'movie')

    def get_movie(self, review):
        return review.movie.title


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = 'movie'.split()


class MovieReviewSerializer(serializers.ModelSerializer):
    director = serializers.SerializerMethodField()
    reviews = ReviewsSerializer(many=True)
    average_rate = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration', 'director', 'reviews', 'average_rate')

    def get_director(self, movie):
        return movie.director.name

    def get_average_rate(self, movie):
        all_stars = [review.stars for review in movie.reviews.all()]
        return sum(all_stars) / len(all_stars) if all_stars else None







