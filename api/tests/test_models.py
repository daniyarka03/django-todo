from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.exceptions import ValidationError
from datetime import date
from api.models import Task
import os
from PIL import Image
import io


class TaskModelTest(TestCase):
    def setUp(self):
        image = Image.new("RGB", (100, 100), color="red")
        img_io = io.BytesIO()
        image.save(img_io, format="JPEG")
        img_io.seek(0)

        self.test_image = SimpleUploadedFile(
            name="test_image.jpg", content=img_io.read(), content_type="image/jpeg"
        )

    def test_create_task_with_valid_data(self):
        task = Task.objects.create(
            title="Test Task",
            description="Test Description",
            due_date=date(2024, 12, 31),
        )
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")

    def test_create_task_with_too_long_title(self):
        with self.assertRaises(ValidationError):
            task = Task(title="A" * 101, description="Valid Description")
            task.full_clean()

    def test_create_task_with_too_long_description(self):
        with self.assertRaises(ValidationError):
            task = Task(title="Valid Title", description="A" * 501)
            task.full_clean()

    def test_create_task_with_image(self):
        task = Task.objects.create(
            title="Task with Image",
            description="Test Description",
            photo=self.test_image,
        )
        self.assertTrue(task.photo)
        self.assertTrue(os.path.exists(task.photo.path))

        img = Image.open(task.photo.path)
        self.assertEqual(img.mode, "L")
        self.assertLessEqual(img.size[0], 800)
        self.assertLessEqual(img.size[1], 800)

    def tearDown(self):
        for task in Task.objects.all():
            if task.photo and task.photo.path:
                if os.path.exists(task.photo.path):
                    try:
                        os.remove(task.photo.path)
                    except PermissionError:
                        pass
