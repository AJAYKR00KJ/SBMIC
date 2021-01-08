from django.db import models


# Create your models here.

class Carousel(models.Model):
    title = models.CharField(max_length=100)
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
    title = models.CharField(max_length=20)
    text = models.TextField()
    date = models.DateTimeField()
    featured = models.BooleanField()

    def __str__(self):
        return self.title


class Youtube(models.Model):
    title = models.CharField(max_length=20)
    date = models.DateTimeField()
    featured = models.BooleanField()
    link_url = models.URLField(max_length=200)

    def __str__(self):
        return self.title

class Announcement(models.Model):
    title = models.CharField(max_length=20)
    date = models.DateTimeField()
    featured = models.BooleanField()
    link_url = models.TextField(max_length=200)

    def __str__(self):
        return self.title

class Tender(models.Model):
    title = models.CharField(max_length=20)
    date = models.DateTimeField()
    featured = models.BooleanField()
    link_url = models.TextField(max_length=200)

    def __str__(self):
        return self.title

class Notice(models.Model):
    title = models.CharField(max_length=20)
    date = models.DateTimeField()
    featured = models.BooleanField()
    link_url = models.TextField(max_length=200)

    def __str__(self):
        return self.title

class Events(models.Model):
    title = models.CharField(max_length=20)
    date = models.DateTimeField()
    featured = models.BooleanField()
    link_url = models.TextField(max_length=200)

    def __str__(self):
        return self.title


class Footer(models.Model):
    college = models.CharField(max_length=40, )
    motive = models.CharField(max_length=100)
    address_txt = models.TextField()
    address_link = models.URLField()
    mobile = models.CharField(max_length=13)
    email = models.EmailField()

