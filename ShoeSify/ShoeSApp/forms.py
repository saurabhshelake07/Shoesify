from  django import forms
from .models import ShoeModel

class ShoeModelForm(forms.ModelForm):
    class Meta:
        model = ShoeModel
        fields = "__all__"

