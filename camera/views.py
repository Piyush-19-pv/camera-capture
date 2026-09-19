from django.shortcuts import render
from django.http import JsonResponse
from .models import CapturedPhoto
import base64
import uuid
from django.core.files.base import ContentFile


def home(request):
    return render(
        request,
        'camera/home.html'
    )


def capture_page(request):
    return render(
        request,
        'camera/capture.html'
    )


def upload_photo(request):

    if request.method == 'POST':

        image_data = request.POST.get('image')

        if not image_data:
            return JsonResponse({
                'success': False,
                'message': 'No image received'
            })

        try:

            format, imgstr = image_data.split(
                ';base64,'
            )

            ext = format.split('/')[-1]

            file_name = f"{uuid.uuid4()}.{ext}"

            photo = CapturedPhoto()

            photo.image.save(
                file_name,
                ContentFile(
                    base64.b64decode(imgstr)
                ),
                save=True
            )

            return JsonResponse({
                'success': True,
                'message': 'Photo uploaded successfully',
                'id': photo.id
            })

        except Exception as e:

            return JsonResponse({
                'success': False,
                'message': str(e)
            })

    return JsonResponse({
        'success': False,
        'message': 'Invalid request'
    })