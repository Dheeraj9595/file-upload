from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'   # title, author, pdf, coverpage ('title', 'author')
        # exclude = ('author',)


        

