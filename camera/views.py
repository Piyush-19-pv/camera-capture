from django.shortcuts import render
from django.http import JsonResponse
from .models import CapturedPhoto
import base64
import uuid
from django.core.files.base import ContentFile


def home(request):
    return render(request, "camera/home.html")


def capture_page(request):
    return render(request, "camera/capture.html")


def upload_photo(request):

    if request.method != "POST":
        return JsonResponse(
            {
                "success": False,
                "message": "Invalid request method"
            },
            status=405
        )

    image_data = request.POST.get("image")

    print("========== PHOTO UPLOAD START ==========")
    print("Image received:", bool(image_data))

    if not image_data:
        print("ERROR: No image received")
        return JsonResponse(
            {
                "success": False,
                "message": "No image received by Django"
            },
            status=400
        )

    try:

        print("Image data length:", len(image_data))

        format, imgstr = image_data.split(";base64,")

        print("Image format:", format)

        ext = format.split("/")[-1]

        file_name = f"{uuid.uuid4()}.{ext}"

        print("File name:", file_name)

        image_bytes = base64.b64decode(imgstr)

        print("Decoded image size:", len(image_bytes), "bytes")

        photo = CapturedPhoto()

        photo.image.save(
            file_name,
            ContentFile(image_bytes),
            save=True
        )

        print("PHOTO SAVED SUCCESSFULLY")
        print("Photo ID:", photo.id)
        print("Photo path:", photo.image.name)
        print("========== PHOTO UPLOAD END ==========")

        return JsonResponse(
            {
                "success": True,
                "message": "Photo uploaded successfully",
                "id": photo.id
            }
        )

    except Exception as e:

        print("========== PHOTO UPLOAD ERROR ==========")
        print("ERROR TYPE:", type(e).__name__)
        print("ERROR MESSAGE:", str(e))
        print("========================================")

        return JsonResponse(
            {
                "success": False,
                "message": f"{type(e).__name__}: {str(e)}"
            },
            status=500
        )