from django.urls import path
from django.views.generic import DeleteView

from crud.views import BookTemplateView, BookDetailView, BookFormView, update_book, delete_book

urlpatterns = [
    path("book/", BookTemplateView.as_view(), name="index"),
    path("book/<int:pk>", BookDetailView.as_view(), name="book"),
    path("form/", BookFormView.as_view(), name="form"),
    path("book/<int:pk>/update", update_book, name="update_book"),
    path("book/<int:pk>/delete_book", delete_book, name="delete")
]
