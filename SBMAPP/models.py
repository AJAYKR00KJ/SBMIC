from django.db import models

# Create your models here.

class Carousel(models.Model):
    title = models.CharField(max_length = 100)
    thumbnail = models.ImageField()
    featured = models.BooleanField()

    def __str__(self):
        return self.title


class Implinks(models.Model):
    link_text = models.CharField(max_length=1000)
    link_url = models.CharField(max_length=1000)
    date = models.DateTimeField()
    featured = models.BooleanField()

    def __str__(self):
        return self.link_text


class Marque(models.Model):
    link_text = models.CharField(max_length=1000)
    link_url = models.CharField(max_length=1000)
    date = models.DateTimeField()
    featured = models.BooleanField()

    def __str__(self):
        return self.link_text

class Welcome(models.Model):
    title= models.CharField(max_length=20)
    text= models.TextField()
    date = models.DateTimeField()
    featured = models.BooleanField()

    def __str__(self):
        return self.title