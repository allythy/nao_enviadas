from django import forms
from colorfield.widgets import ColorWidget

from .models import Letter


class LetterForm(forms.ModelForm):
    class Meta:
        model = Letter
        fields = ('name', 'message', 'color')

        labels = {
            'name': 'Para',
            'message': 'Mensagem',
            'color': 'Cor'
        }
