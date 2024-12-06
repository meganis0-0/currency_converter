from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        # Проверяем, существует ли уже пользователь с таким именем
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Это имя пользователя уже занято.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        # Проверяем, соответствует ли пароль минимальным требованиям
        if len(password) < 6:
            raise forms.ValidationError("Пароль должен содержать минимум 6 символов.")
        return password