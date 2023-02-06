from django.test import TestCase
# Book이 있다고 치고
from .models import Book

class ModelTest(TestCase):
    #테스트를 수행하기 전에 호출되는 함수
    def setup(self):
        self.book_title = "MyBook"
        self.book_author = "ADAM"
        self.book = Book(title=self.book_title, author=self.book_author)

    #테스트를 하기 위한 함수
    def test_model_can_create_a_bucketlist(self):
        old_count = Book.objects.count()
        self.book.save()
        new_count = Book.objects.count()
        self.assertNotEqual(old_count, new_count)

from rest_framework.test import APIClient
from rest_framework import status

class ViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book_data = {"title":"MyBook", "author":"soosoo"}
        self.response = self.client.post('/api/books/',
                                         self.book_data, format="json")

    # 실제 테스트에 사용되는 함수
    def test_api_cam_create_a_book(self):
        print(self.response.content)
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)