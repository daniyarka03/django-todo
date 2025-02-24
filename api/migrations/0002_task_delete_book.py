# Generated by Django 5.1.6 on 2025-02-15 08:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=100,
                        validators=[django.core.validators.MaxLengthValidator(100)],
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        max_length=500,
                        validators=[django.core.validators.MaxLengthValidator(500)],
                    ),
                ),
                ("due_date", models.DateField(blank=True, null=True)),
                (
                    "photo",
                    models.ImageField(blank=True, null=True, upload_to="task_photos/"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name="Book",
        ),
    ]
