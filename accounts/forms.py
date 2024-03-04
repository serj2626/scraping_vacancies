from cProfile import label
from django import forms
from django.contrib.auth import authenticate, get_user_model
from scraping.models import Language, City


User = get_user_model()


class UserLoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = 'Почта'
        self.fields['password'].label = 'Пароль'

    def clean(self):
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]
        user = User.objects.filter(email=email).first()

        if not user or not user.check_password(password):
            raise forms.ValidationError(
                "Неверная почта или пароль. Повторите попытку.")

        return super().clean()


class UserRegistrationForm(forms.ModelForm):
    email = forms.CharField(label='Почта', widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(
        label='Пароль', widget=forms.PasswordInput(
            attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        label='Повторите пароль', widget=forms.PasswordInput(
            attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('email', 'password', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError(
                "Пользователь с такой почтой уже существует")
        return email

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']


class UserUpdateForm(forms.ModelForm):

    # city = forms.ModelChoiceField(
    #     queryset=City.objects.all(), label='Город',
    #     required=False, to_field_name='slug',
    #     widget=forms.Select(attrs={'class': 'form-control'}))

    city = forms.ModelChoiceField(label='Город',
                                  queryset=City.objects.all())
    language = forms.ModelChoiceField(
        label='Язык программирования', queryset=Language.objects.all())

    # language = forms.ModelChoiceField(

    #     queryset=Language.objects.all(), label='Специальность',
    #     required=False, to_field_name='slug',
    #     widget=forms.Select(attrs={'class': 'form-control'}))

    send_email = forms.BooleanField(
        label='Получать рассылку?', required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    class Meta:
        model = User
        fields = ('city', 'language', 'send_email')
