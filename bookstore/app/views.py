from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response   
from rest_framework import status  
from .models import Book
from .serializers import BookSerializer

# Create your views here.

# /api/books/
class BookListView(APIView):
    def get(self,request):
        all_books = Book.objects.all()
        serializer = BookSerializer(all_books, many=True)
        return Response(serializer.data)
    
    def post (self,request):
        requested_data = request.data
        serializer = BookSerializer(data = requested_data)
        # make decision to save the book is valid and return a status to the user!
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
