from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_media, name='upload_media'),
    path('delete_media/<str:media_type>/<int:media_id>/', views.delete_media, name='delete_media'),
]