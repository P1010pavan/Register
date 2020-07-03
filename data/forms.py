from django import forms
from django.forms import ModelForm
from . models import Detail

class Regist(forms.ModelForm):
    class Meta:
        model = Detail
        fields = '__all__'