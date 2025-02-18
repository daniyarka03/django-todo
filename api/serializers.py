from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "due_date",
            "photo",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
        extra_kwargs = {
            'title': {'required': False},  
        }

    def validate(self, data):
        if self.instance is None and not data.get('title'):
            raise serializers.ValidationError({"title": "This field is required when creating a task."})
        return data