from django.urls import path
from .views import login_view, register_view, convert_currency_view, logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('convert/', convert_currency_view, name='convert'),
    path('logout/', logout_view, name='logout'),  # Добавляем маршрут для выхода

]