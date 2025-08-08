from django.urls import path
from .views import BookView
from .views import BookDetailView

# app_name = 'api'
urlpatterns = [
    path(
        "books/",BookView.as_view(),name='book-list'
    ),
    path(
        "books/<int:id>",BookDetailView.as_view(),name='books-detail'
    ),
]


