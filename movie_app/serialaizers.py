from rest_framework import serializers
from movie_app.models import Director, Movie, Review
from rest_framework.exceptions import ValidationError


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
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration', 'director', 'reviews', 'rating')

    def get_director(self, movie):
        return movie.director.name

    def get_rating(self, movie):
        all_stars = [review.stars for review in movie.reviews.all()]
        return sum(all_stars) / len(all_stars) if all_stars else None


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=2, max_length=20)


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=3, max_length=20)
    description = serializers.CharField(min_length=10)
    duration = serializers.IntegerField(min_value=30)
    director = serializers.IntegerField(min_value=1)

    def validate_director(self, director):
        try:
            Director.objects.get(id=director)
        except Director.DoesNotExist:
            raise ValidationError('Director not found')
        return director


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=3, max_length=255)
    movie = serializers.IntegerField(min_value=1)
    stars = serializers.IntegerField(min_value=1, max_value=5)

    def validate_movie(self, movie):
        try:
            Movie.objects.get(id=movie)
        except Movie.DoesNotExist:
            raise ValidationError('Movie not found')
        return movie




