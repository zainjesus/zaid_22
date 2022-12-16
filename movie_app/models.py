from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=15)


class Movie(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    duration = models.DurationField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
