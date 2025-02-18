from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, LeetCodeViewSet

router = DefaultRouter()
router.register(r"tasks", TaskViewSet)
router.register(r"leetcode", LeetCodeViewSet, basename="leetcode")

urlpatterns = [
    path("", include(router.urls)),
]
