from django.urls import path
from .views import logout_view, login_view, register_view, UserUpdateView

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('profile/<int:pk>/', UserUpdateView.as_view(), name='profile'),
]
