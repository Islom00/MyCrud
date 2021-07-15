from django.urls import path

from crud.views import BookTemplateView, BookDetailView, BookFormView

urlpatterns = [
    path("book/", BookTemplateView.as_view(), name="index"),
    path("book/<int:pk>", BookDetailView.as_view(), name="book"),
    path("form/", BookFormView.as_view(), name="form")
]