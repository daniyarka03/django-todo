from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from .services import rotate_array, find_kth_largest, longest_increasing_path
from django.utils import timezone


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Task deleted successfully."}, status=status.HTTP_200_OK
        )

    @action(detail=False, methods=["get"], url_path="nearest-deadline")
    def nearest_deadline(self, request):
        today = timezone.now().date()
        task = (
            Task.objects.filter(due_date__isnull=False, due_date__gte=today)
            .order_by("due_date")
            .first()
        )

        if not task:
            return Response(
                {"detail": "No tasks with future deadlines found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.get_serializer(task)
        return Response(serializer.data)


class LeetCodeViewSet(viewsets.ViewSet):
    @action(detail=False, methods=["post"], url_path="rotate-array")
    def rotate_array(self, request):
        nums = request.data.get("nums", [])
        k = request.data.get("k", 0)

        if not isinstance(nums, list) or not all(isinstance(x, int) for x in nums):
            return Response(
                {"error": "Invalid input: nums must be a list of integers"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not isinstance(k, int) or k < 0:
            return Response(
                {"error": "Invalid input: k must be a non-negative integer"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        result = rotate_array(nums.copy(), k)
        return Response({"result": result})

    @action(detail=False, methods=["post"], url_path="kth-largest")
    def kth_largest(self, request):
        nums = request.data.get("nums", [])
        k = request.data.get("k", 0)

        try:
            result = find_kth_largest(nums, k)
            return Response({"result": result})
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["post"], url_path="longest-increasing-path")
    def longest_increasing_path(self, request):
        matrix = request.data.get("matrix", [])

        if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix
        ):
            return Response(
                {"error": "Invalid input: matrix must be a 2D array"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        result = longest_increasing_path(matrix)
        return Response({"result": result})
