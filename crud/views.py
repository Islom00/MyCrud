from django.views.generic import ListView, DetailView, FormView

from .forms import BookModelForm
from .models import *


class BookTemplateView(ListView):
    template_name = "index.html"
    model = BookModel

class BookDetailView(DetailView):
    template_name = "detail.html"
    model = BookModel


class BookFormView(FormView):
    template_name = "forms.html"
    form_class = BookModelForm
    success_url = "/book/"