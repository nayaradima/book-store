from django.urls import path
from .views import BookListView

# app_name = 'api'
urlpatterns = [
    path(
        "books/",BookListView.as_view(),name='books'
    ),
]


