from django.urls import path
from .users import register, login
from .currency import exchange_rates, convert

urlpatterns = [
    path('auth/register/', register, name="register"),
    path('auth/login/', login, name="login"),
    path('currency/exchange/', exchange_rates, name="exchange_rates"),
    path('currency/convert/', convert, name="convert"),
]