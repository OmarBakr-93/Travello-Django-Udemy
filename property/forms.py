from django import forms
from .models import Property_Book


class PropertyBookForm(forms.ModelForm):
  class Meta:
    model = Property_Book
    fields = ['date_from', 'date_to', 'guest', 'children']