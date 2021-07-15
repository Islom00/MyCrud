from django import forms

from crud.models import BookModel


class BookModelForm(forms.ModelForm):
    class Meta:
        model = BookModel
        exclude = ["created_at"]