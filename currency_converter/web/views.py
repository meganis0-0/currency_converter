import requests
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm
from currency.external_api import get_exchange_rates, convert_currency
import os
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env, который находится в корне проекта.
load_dotenv()

API_URL = os.getenv("API_URL")
def login_view(request):
    if request.user.is_authenticated:
        return redirect('convert')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('convert')
            else:
                # Если аутентификация не удалась, передаем сообщение об ошибке
                error_message = "Неверный логин или пароль."
                return render(request, 'web/login.html', {'form': form, 'error': error_message})
    else:
        form = LoginForm()
    
    return render(request, 'web/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, password=password)
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'web/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def convert_currency_view(request):
    rates = get_exchange_rates()  # Получаем курсы валют

    if request.method == 'POST':
        amount = request.POST.get('amount')
        from_currency = request.POST.get('from_currency').upper()  # Приводим к верхнему регистру
        to_currency = request.POST.get('to_currency').upper()      # Приводим к верхнему регистру

        # Проверяем, что все поля заполнены
        if not amount or not from_currency or not to_currency:
            return render(request, 'web/convert.html', {
                'error': 'Пожалуйста, заполните все поля.',
                'rates': rates
            })

        try:
            amount = float(amount)  # Преобразуем сумму в число
        except ValueError:
            return render(request, 'web/convert.html', {
                'error': 'Сумма должна быть числом.',
                'rates': rates
            })

        # Проверяем наличие валют в курсах
        if from_currency not in rates or to_currency not in rates:
            return render(request, 'web/convert.html', {
                'error': 'Недопустимые валюты.',
                'rates': rates
            })

        # Конвертация валюты
        try:
            converted_amount = convert_currency(amount, from_currency, to_currency)
            return render(request, 'web/convert.html', {
                'converted_amount': converted_amount,
                'amount': amount,
                'from_currency': from_currency,
                'to_currency': to_currency,
                'rates': rates
            })
        except Exception as e:
            return render(request, 'web/convert.html', {
                'error': str(e),  # Выводим текст ошибки
                'rates': rates
            })

    return render(request, 'web/convert.html', {'rates': rates})  # Передаем курсы валют в шаблон