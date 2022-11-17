from myapp.models import *
from django import forms


class TEXTTOHTMLFORM(forms.ModelForm):
    class Meta:
        model = TextConverter
        fields = '__all__'