from django.test import TestCase

# Create your tests here.

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from app.models import Book
from app.serializers import BookSerializer

class BookApiViewTest(APITestCase):
    
    
    def setUp(self):
        # Create a dummy data to use in tests
        Book.objects.create(
            title="Testing Title",
            author="FirstName LastName",
            isbn="8274509872645",
            published_date="2025-01-01"
        )
        self.url = reverse('books')
        
    def testGetBook(self):
        # retriving data -> read
        response = self.client.get(self.url, format='json')
        assert response.status_code == status.HTTP_200_OK
        
        booksAll = Book.objects.all()
        expected_data = BookSerializer(booksAll, many=True).data
        assert response.json() == expected_data
        
    def testCreateValidBook(self):
        # creating data -> post method
        data = {
            "title": "Finding Me",
            "author": "Viola Davis",
            "isbn": "1927452098445",
            "published_date": "22/04/2022"
            }
        response = self.client.post(self.url,data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        
        created_book = Book.objects.last()
        expected_data = BookSerializer(created_book).data
        assert response.json() == expected_data
        
    def testCreateInvalidBook(self):
        data = {
            "title": "", # Required filed (book has to have a title)
            "author": "Unknown",
            "isbn": "invalidisbn", # Only numbers and has to be 13 digits
            "published_date": "not a format of date dd-mm-yyyy"
            }
        response = self.client.post(self.url, data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        

        
        
        
        
        
        
    
        