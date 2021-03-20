from django import forms

from .models import Letter


class LetterForm(forms.ModelForm):
    class Meta:
        model = Letter
        fields = ('name', 'message')

        labels = {
            'name': 'Para',
            'message': 'Mensagem'
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'input'}),
            'message': forms.Textarea(attrs={'class': 'textarea'})
        }
