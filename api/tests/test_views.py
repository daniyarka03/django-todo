from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Task
from datetime import date, timedelta
from django.utils import timezone


class TaskViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task_data = {
            "title": "Test Task",
            "description": "Test Description",
            "due_date": "2024-12-31",
        }
        self.task = Task.objects.create(
            title="Existing Task",
            description="Existing Description",
            due_date=date(2024, 12, 31),
        )

    def test_nearest_deadline(self):
        Task.objects.all().delete()

        today = timezone.now().date()

        Task.objects.create(
            title="Future Task",
            description="Future Description",
            due_date=today + timedelta(days=30),
        )

        nearest_task = Task.objects.create(
            title="Nearest Task",
            description="Nearest Description",
            due_date=today + timedelta(days=1),
        )

        Task.objects.create(
            title="Past Task",
            description="Past Description",
            due_date=today - timedelta(days=1),
        )

        response = self.client.get(reverse("task-nearest-deadline"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Nearest Task")
        self.assertEqual(response.data["id"], nearest_task.id)
