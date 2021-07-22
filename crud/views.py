from django.shortcuts import get_object_or_404, redirect, render
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


def update_book(request, pk):
    if request.method == "POST":
        book = get_object_or_404(BookModel, pk=pk)
        form = BookModelForm(request.POST, files=request.FILES, instance=book)

        if form.is_valid():
            form.save()

        return redirect("/book/")
    else:
        book = get_object_or_404(BookModel, pk=pk)
        form = BookModelForm(instance=book)

    context = {
        "form": form
    }
    return render(request, "forms.html", context)


def delete_book(request, pk):
    book = get_object_or_404(BookModel, pk=pk)
    book.delete()
    return redirect("/book/")
