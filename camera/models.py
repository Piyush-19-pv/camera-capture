from django.db import models


class CapturedPhoto(models.Model):
    image = models.ImageField(upload_to='captured/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo {self.id} - {self.created_at}"