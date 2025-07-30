from rest_framework import serializers
from .models import Book  

# In case i dont want to get the .modelSerializer I can do another kind of:
# class BookSerializer(serializers.Serializer):
#     title = serializer.CharField() --> write the exactly same i wrote in the other file. 

class BookSerializer(serializers.ModelSerializer):
    published_date = serializers.DateField(format="%d/%m/%Y")
    
    class Meta:
        model = Book
        fields = [ 'title','author','isbn','published_date']