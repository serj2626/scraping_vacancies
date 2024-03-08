from .models import Vacancy
from django.db.models import Q
from django.core.mail import EmailMultiAlternatives


def get_filter_vacancys(city, language):
    if city and language:
        vacancys = Vacancy.objects.filter(
            Q(city__slug=city) & Q(language__slug=language))
        if vacancys.exists():
            return vacancys

    elif city or language:
        vacancys = Vacancy.objects.filter(city__slug=city) if city else Vacancy.objects.filter(
            language__slug=language)
        if vacancys.exists():
            return vacancys

    elif not city and not language:
        return Vacancy.objects.all()
