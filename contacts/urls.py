from django.urls import path
from .views import FeedbackView


app_name = 'contacts'

urlpatterns = [
    path('feedback/', FeedbackView.as_view(), name='feedback'),
]
