from django import forms
from .models import Image, Video, Audio


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image']


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'video']


class AudioForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ['title', 'audio']
