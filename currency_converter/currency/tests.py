from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from unittest.mock import patch

class UserTests(APITestCase):

    def test_register_user(self):
        url = reverse('register')
        data = {'username': 'testuser', 'password': 'testpass'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)  # Ожидаем редирект на страницу логина

    def test_login_user(self):
        User.objects.create_user(username='testuser', password='testpass')
        url = reverse('login')
        data = {'username': 'testuser', 'password': 'testpass'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)  # Ожидаем редирект после успешного входа

class CurrencyTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')


    def test_convert_currency_invalid(self):
        url = reverse('convert')

        # Проверка на недопустимую валюту
        data = {'amount': 100, 'from_currency': 'INVALID', 'to_currency': 'EUR'}

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  # Ожидаем статус 400 при неверной валюте


    # @patch('currency.externalapi.get_exchange_rates')
    # def test_exchange_rates(self, mock_get_exchange_rates):
    #     # Настраиваем мок для возврата фиктивных данных о курсах валют
    #     mock_get_exchange_rates.return_value = {
    #         "USD": {"Value": 100.0, "Nominal": 1},
    #         "EUR": {"Value": 120.0, "Nominal": 1},
    #         "RUB": {"Value": 1.0, "Nominal": 1}
    #     }

    #     url = reverse('convert')  # Убедитесь в правильности URL для получения курсов валют
    #     response = self.client.get(url)

    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertIn("USD", response.content.decode())  # Проверяем наличие USD в ответе

    # @patch('currency.externalapi.convert_currency')
    # def test_convert_currency(self, mock_convert_currency):
    #     # Настраиваем мок для возврата фиктивного значения конвертации
    #     mock_convert_currency.return_value = 120.0
        
    #     url = reverse('convert')
    #     data = {'amount': 100, 'from_currency': 'USD', 'to_currency': 'EUR'}
        
    #     response = self.client.post(url, data)

    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.context['converted_amount'], 120.0)  # Проверяем результат конвертации

    def test_convert_currency_invalid(self):
        url = reverse('convert')

        # Проверка на недопустимую валюту
        data = {'amount': 100, 'from_currency': 'INVALID', 'to_currency': 'EUR'}

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Ожидаем статус 200 при неверной валюте