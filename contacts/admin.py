from django.contrib import admin
from .models import FeedBack

@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    '''Admin View for FeedBack)'''

    list_display = ('user', 'subject', 'date_create')
