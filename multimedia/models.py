from django.db import models


class Image(models.Model):
    """ model for images """
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')


class Video(models.Model):
    """ model for videos """
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')


class Audio(models.Model):
    """ model for audios """
    title = models.CharField(max_length=100)
    audio = models.FileField(upload_to='audios/')
