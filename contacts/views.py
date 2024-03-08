from django.shortcuts import render
from django.core.mail import send_mail
from .forms import FeedBackForm
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import FeedBack
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from scraping_service.settings import EMAIL_HOST_USER

class FeedbackView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    
    template_name = 'contacts/feedback.html'
    form_class = FeedBackForm
    success_message = 'Вы успешно оставили свою заявку!'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        send_mail(
            subject=form.cleaned_data['subject'],
            message=form.cleaned_data['message'],
            from_email=EMAIL_HOST_USER,
            recipient_list=[user],
            fail_silently=False
        )
        return super().form_valid(form)
    

