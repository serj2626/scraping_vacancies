from django import forms
from .models import FeedBack


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = ('subject', 'message')
        labels = {
            'subject': 'Тема',
            'message': 'Сообщение',
        }
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
