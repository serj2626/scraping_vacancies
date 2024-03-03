from django.db import models
from pytils.translit import slugify
from django.utils.text import slugify as sl


class City(models.Model):
    '''Model definition for City.'''

    name = models.CharField('название города', max_length=50, unique=True)
    number_id = models.PositiveIntegerField('номер в списке', unique=True, null=True)
    slug = models.SlugField('слаг', blank=True, unique=True)

    class Meta:
        '''Meta definition for City.'''

        verbose_name = 'City'
        verbose_name_plural = 'Citys'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        Метод формирует слаг
        """
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Language(models.Model):
    '''Model definition for Language.'''
    name = models.CharField('язык программирования',
                            max_length=50, unique=True)
   
    slug = models.SlugField('слаг', blank=True, unique=True)

    class Meta:
        '''Meta definition for Language.'''

        verbose_name = 'Language'
        verbose_name_plural = 'Languages'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        Метод формирует слаг
        """
        if not self.slug:
            self.slug = sl(self.name)
        return super().save(*args, **kwargs)


class Vacancy(models.Model):
    '''Model definition for Vacancy.'''

    url = models.URLField('ссылка', unique=True)
    title = models.CharField('Название', max_length=250)
    company = models.CharField('компания', max_length=250)
    description = models.TextField('описание вакансии')
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, verbose_name='город')
    language = models.ForeignKey(
        Language, on_delete=models.CASCADE, verbose_name='язык программирования')
    timestamp = models.DateField('дата добавления вакансии', auto_now_add=True)

    class Meta:
        '''Meta definition for Vacancy.'''

        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancys'

    def __str__(self):
        return f'Вакансия {self.title} | город {self.city.name}'
