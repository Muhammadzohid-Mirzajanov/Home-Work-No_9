from django import forms
from .models import Flower, Type

class FlowerForm(forms.ModelForm):
    class Meta:
        model = Flower
        fields = ['name', 'type', 'description']

class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']
