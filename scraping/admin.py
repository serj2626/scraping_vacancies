from django.contrib import admin
from .models import City, Language, Vacancy


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('name', 'number_id', 'slug')


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('name', 'slug')


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    '''Admin View for Vacancy'''

    list_display = ( 'title', 'company',
                    'city', 'language', 'timestamp', 'url',)
