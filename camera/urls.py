from django.urls import path
from . import views


urlpatterns = [

    # Front page
    path(
        '',
        views.home,
        name='home'
    ),

    # Camera page
    path(
        'capture/',
        views.capture_page,
        name='capture'
    ),

    # Upload
    path(
        'upload/',
        views.upload_photo,
        name='upload_photo'
    ),

]