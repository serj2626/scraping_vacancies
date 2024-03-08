from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserLoginForm, UserRegistrationForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView

User = get_user_model()


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('accounts:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            login(request, user)
            messages.success(request, 'Вы успешно вошли в систему!')
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли из системы!')
    return redirect('home')


# class LogoutUserView(LoginRequiredMixin, SuccessMessageMixin, LogoutView):
#     next_page = reverse_lazy('accounts:login')
#     success_message = 'Вы успешно вышли из системы!'


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_message = 'Профиль успешно обновлен'
    template_name = "accounts/profile.html"

    def get_success_url(self):
        print(self.kwargs)
        return reverse('accounts:profile', kwargs={'pk': self.kwargs['pk']})
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feedback_list'] =  self.get_object().user_feedback.all()
        return context
    
