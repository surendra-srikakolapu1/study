from django.db import models

# Create your models here.

class Django(models.Model):
    title = models.CharField(max_length=1000)
    definition = models.TextField(max_length=2000,blank=True)
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Json(models.Model):
    title = models.CharField(max_length=1000)
    definition = models.TextField(max_length=2000,blank=True)
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Rest(models.Model):
    title = models.CharField(max_length=1000)
    definition = models.TextField(max_length=2000,blank=True)
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Html(models.Model):
    title = models.CharField(max_length=1000)
    definition = models.TextField(max_length=2000,blank=True)
    image = models.ImageField(null=True,blank=True,upload_to="media/pics")

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Css(models.Model):
    title = models.CharField(max_length=1000)
    definition = models.TextField(max_length=2000,blank=True)
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Bootstrap(models.Model):
    title = models.CharField(max_length=1000)
    definition = models.TextField(max_length=2000,blank=True)
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Python(models.Model):
    title = models.CharField(max_length=1000)
    definition = models.TextField(max_length=2000,blank=True)
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Js(models.Model):
    title = models.CharField(max_length=1000)
    definition = models.TextField(max_length=2000,null=True,blank=True)
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
