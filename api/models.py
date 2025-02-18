from django.db import models
from django.core.validators import MaxLengthValidator
from django.core.files.base import ContentFile
from PIL import Image
import io


class Task(models.Model):
    title: models.CharField = models.CharField(
        max_length=100,
        validators=[MaxLengthValidator(100)],
    )
    description: models.TextField = models.TextField(
        max_length=500,
        blank=True,
        null=True,
        validators=[MaxLengthValidator(500)],
    )
    due_date: models.DateField = models.DateField(null=True, blank=True)
    photo: models.ImageField = models.ImageField(
        upload_to="task_photos/", null=True, blank=True
    )
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs) -> None:
        if self.photo and hasattr(self.photo, "file"):
            try:
                if not self.pk or self.photo != Task.objects.get(pk=self.pk).photo:
                    image: Image.Image = Image.open(self.photo)

                    image = image.convert("L")

                    if image.width > 800 or image.height > 800:
                        image.thumbnail((800, 800), Image.Resampling.LANCZOS)

                    output = io.BytesIO()
                    image.save(output, format="JPEG", quality=75)  
                    output.seek(0)

                    self.photo.save(self.photo.name, ContentFile(output.read()), save=False)

            except Exception as e:
                print(f"Error processing image: {e}")

        super().save(*args, **kwargs) 


    def __str__(self) -> str:
        return self.title
