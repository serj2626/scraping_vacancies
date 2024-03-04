from django import forms
from .models import Vacancy, City, Language


class VacancyForm(forms.Form):
    city = forms.ModelChoiceField(
        queryset=City.objects.all(), label='Город',
        required=False, to_field_name='slug')
    language = forms.ModelChoiceField(
        queryset=Language.objects.all(), label='Язык программирования',
        required=False, to_field_name='slug')


