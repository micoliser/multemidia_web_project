from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageForm, VideoForm, AudioForm
from .models import Image, Video, Audio


def upload_media(request):
    image_form = ImageForm()
    video_form = VideoForm()
    audio_form = AudioForm()

    if request.method == 'POST':
        if 'image' in request.POST:
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('upload_media')

        elif 'video' in request.POST:
            form = VideoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('upload_media')

        elif 'audio' in request.POST:
            form = AudioForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('upload_media')
    else:
        images = Image.objects.all()
        videos = Video.objects.all()
        audios = Audio.objects.all()

        return render(request, 'multimedia/index.html', {
            'image_form': image_form,
            'video_form': video_form,
            'audio_form': audio_form,
            'images': images,
            'videos': videos,
            'audios': audios,
        })


def delete_media(request, media_type, media_id):
    media_type = media_type.lower()
    if media_type not in ['image', 'video', 'audio']:
        return redirect('upload_media')

    model_class = {'image': Image, 'video': Video, 'audio': Audio}.get(media_type)
    media_item = get_object_or_404(model_class, id=media_id)

    if request.method == 'POST':
        media_item.delete()

    return redirect('upload_media')