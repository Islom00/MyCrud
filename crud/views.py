from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, FormView, CreateView, DeleteView

from .forms import BookModelForm
from .models import *


class BookTemplateView(ListView):
    template_name = "index.html"
    model = BookModel


class BookDetailView(DetailView):
    template_name = "detail.html"
    model = BookModel


class BookFormView(CreateView):
    template_name = "forms.html"
    form_class = BookModelForm
    success_url = "/book/"

    def form_valid(self, form):
        return super(BookFormView, self).form_valid(form)
