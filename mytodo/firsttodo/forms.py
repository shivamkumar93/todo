from django  import forms
from .models import Todo

class Todoform(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title","description","completed"]
    