from .models import Book
from django import forms

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['title','author','description','published_year']

