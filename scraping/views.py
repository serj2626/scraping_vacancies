from django.shortcuts import render
from django.views.generic import View
from .forms import VacancyForm
from .service import get_filter_vacancys
from .models import Vacancy
from django.contrib import messages

class HomeView(View):

    def get(self, request):
        form = VacancyForm(request.GET)
        city = request.GET.get('city', '')
        language = request.GET.get('language', '')
        vacancys = get_filter_vacancys(city, language)

        context = {
            'vacancys': vacancys,
            'title': 'Главная страница',
            'form': form
        }
        return render(request=request, template_name="scraping/home.html", context=context)

