from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Profile(models.Model):
    email = models.EmailField('Email')
    age = models.IntegerField(
        'Age',
        validators=(
            MinValueValidator(12),
        )
    )
    password = models.CharField(
        'Password',
        max_length=30,
    )
    first_name = models.CharField(
        'First Name',
        max_length=30,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        'Last Name',
        max_length=30,
        null=True,
        blank=True
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Model(models.Model):
    title = models.CharField(
        'Title',
        max_length=30,
        unique=True,
    )
    category = models.CharField(
        'Category',
        choices=(("Action", "Action"), ("Adventure", "Adventure"),
                 ("Puzzle", "Puzzle"), ("Strategy", "Strategy"), ("Sports", "Sports"),
                 ("Board/Card Game", "Board/Card Game"), ("Other", "Other")),
        max_length=15,
    )
    rating = models.FloatField(
        'Rating',
        validators=[MinValueValidator(0.1), MaxValueValidator(5.0)]
    )
    max_level = models.IntegerField(
        'Max Level',
        null=True,
        blank=True,
        validators=[MinValueValidator(1),]
    )
    image_url = models.URLField(
        'Image URL'
    )
    summary = models.TextField(
        'Summary',
        null=True,
        blank=True,
    )