from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CapturedPhoto


@admin.register(CapturedPhoto)
class CapturedPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'created_at')
    list_display_links = ('id',)
    ordering = ('-created_at',)