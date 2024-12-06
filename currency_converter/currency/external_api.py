import requests
import os
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env, который находится в корне проекта.
load_dotenv()

def get_exchange_rates():
    # URL API ЦБ для получения курсов валют
    url = os.getenv("EXTERNAL_API_URL")
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception("Ошибка при получении курсов валют")
    
    data = response.json()
    
    # Добавляем информацию о рубле (RUB) в данные
    rub_rate = {
        "ID": "R01239",                 # ID для RUB
        "NumCode": "643",               # Код для RUB
        "CharCode": "RUB",              # Символ для RUB
        "Nominal": 1,                   # Номинал
        "Name": "Российский рубль",     # Название
        "Value": 1.0,                   # Стоимость RUB в RUB (1 к 1)
        "Previous": 1.0                 # Предыдущая стоимость (для примера)
    }
    
    data['Valute']['RUB'] = rub_rate  # Добавляем RUB в словарь с валютами
    
    return data['Valute']  # Возвращаем только словарь с курсами валют

def convert_currency(amount, from_currency, to_currency):
    rates = get_exchange_rates()  # Получаем курсы валют

    # Проверяем, есть ли нужные валюты в данных
    if from_currency not in rates or to_currency not in rates:
        raise ValueError("Недопустимая валюта")

    if from_currency == 'RUB':
        # Если мы конвертируем из рублей в другую валюту
        to_rate = rates[to_currency]['Value'] / rates[to_currency]['Nominal']
        converted_amount = amount / to_rate  # amount в RUB -> amount в другой валюте
    elif to_currency == 'RUB':
        # Если мы конвертируем в рубли
        from_rate = rates[from_currency]['Value'] / rates[from_currency]['Nominal']
        converted_amount = amount * from_rate  # amount в другой валюте -> amount в RUB
    else:
        # Общий случай: конвертация между двумя валютами
        from_rate = rates[from_currency]['Value'] / rates[from_currency]['Nominal']
        to_rate = rates[to_currency]['Value'] / rates[to_currency]['Nominal']
        converted_amount = (from_rate / to_rate) * amount

    if converted_amount < 0:
        raise ValueError("Недопустимая сумма")
    
    return converted_amount