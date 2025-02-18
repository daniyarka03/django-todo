from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.test import TestCase


class LeetCodeViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_rotate_array(self):
        data = {"nums": [1, 2, 3, 4, 5, 6, 7], "k": 3}
        response = self.client.post(
            reverse("leetcode-rotate-array"), data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["result"], [5, 6, 7, 1, 2, 3, 4])

    def test_rotate_array_invalid_input(self):
        invalid_data = {"nums": "not a list", "k": 3}
        response = self.client.post(
            reverse("leetcode-rotate-array"), invalid_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_kth_largest(self):
        data = {"nums": [3, 2, 1, 5, 6, 4], "k": 2}
        response = self.client.post(
            reverse("leetcode-kth-largest"), data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["result"], 5)

    def test_kth_largest_invalid_k(self):
        invalid_data = {"nums": [1, 2, 3], "k": 4}
        response = self.client.post(
            reverse("leetcode-kth-largest"), invalid_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_longest_increasing_path(self):
        data = {"matrix": [[9, 9, 4], [6, 6, 8], [2, 1, 1]]}
        response = self.client.post(
            reverse("leetcode-longest-increasing-path"), data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["result"], 4)

    def test_longest_increasing_path_invalid_input(self):
        invalid_data = {"matrix": "not a matrix"}
        response = self.client.post(
            reverse("leetcode-longest-increasing-path"), invalid_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
