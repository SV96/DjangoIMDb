from django.db import models
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.

CATEGORY_CHOICES = (
    ('action', 'ACTION'),
    ('comedy', 'COMEDY'),
    ('drama', 'DRAMA'),
    ('romance', 'ROMANCE'),
)

LANGUAGE_CHOICES = (
    ('english', 'ENGLISH'),
    ('german', 'GERMAN'),
)

STATUS_CHOICES = (
    ('RE', 'RECENTLY ADDED'),
    ('MW', 'MOSTLY WATCHED'),
    ('TR', 'TOP RATED'),
)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='movies')
    banner = models.ImageField(upload_to='movies_banner')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=20)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
    cast = models.CharField(max_length=100)
    year_of_production = models.DateField()
    views_count = models.IntegerField(default=0)


    movie_trailer = models.URLField()

    created = models.DateTimeField(default=timezone.now)

    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


LINK_CHOICES = (
    ('D', 'Downalod link'),
    ('W', 'Watch link'),
)


class MovieLinks(models.Model):
    movie = models.ForeignKey('Movie', related_name='movie_watch_link', on_delete=models.CASCADE)
    type = models.CharField(choices=LINK_CHOICES, max_length=1)
    link = models.URLField()

    def __str__(self):
        return str(self.movie)


