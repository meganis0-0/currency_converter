# Currency Converter App

## Features
Это веб-приложение на Django для обмена валют, которое включает:
- Форму для конвертации валют.
- Таблицу с текущими курсами валют.
- REST API с JWT-аутентификацией для доступа к конвертации валют и получения списка валют.
- Модульные тесты для проверки функционала приложения.
- Использование [внешнего API](https://www.cbr-xml-daily.ru/daily_json.js) для получения списка валют. Загрузка моделей (currency/models.py) при запуске
- Использование конфигурации `.env` <br>

---

## Установка

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/meganis0-0/currency_converter
   cd <repository-directory>
   ```

2. **Создайте и активируйте виртуальное окружение:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Linux/Mac
   venv\Scripts\activate     # Для Windows
   ```

3. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Создайте файл .env в корне проекта и добавьте свои конфиденциальные переменные**

5. **Выполните миграции базы данных:**
   ```bash
   python manage.py migrate
   ```

6. **Запустите сервер разработки:**
   ```bash
   python manage.py runserver
   ```

## Основные возможности
1. **Авторизация и регистрация**:
   - Размещены по адресу `web/login/` и `web/login/`
     ![image](https://github.com/user-attachments/assets/bfd4a279-2208-4a7f-9a7b-0d6ed9a05721)

3. **Форма конвертации валют**:

![image](https://github.com/user-attachments/assets/907db698-d16b-4916-bf2d-a04b1f280297)

   - Размещена по адресу `/web/convert/`.
   - Поля для заполнения:
     - **from**: валюта, из которой будет осуществляться конвертация.
     - **to**: валюта, в которую будет осуществляться конвертация.
     - **amount**: количество конвертируемой валюты.
   - Результат конвертации отображается после заполнения формы.

4. **Таблица с курсами валют**:
   - Размещена на странице `/web/convert/`.
   - Отображает текущие курсы валют относительно рубля.

![image](https://github.com/user-attachments/assets/6108a473-8816-461f-b108-b16f169e5439)


---

## Использование API
- Регистрация пользователя
  
   URL: /api/auth/register/
   Метод: POST
   Тело запроса:
   
   ```json
   {
       "username": "your_username",
       "password": "your_password"
   }
   ```
   
   Ответ:
   
   ```json
   {
       "message": "Пользователь успешно создан"
   }
   ```

- Вход пользователя
  
   URL: /api/auth/login/
   Метод: POST
   Тело запроса:
   
   ```json
   {
       "username": "your_username",
       "password": "your_password"
   }
   ```
   
   Ответ (успешно):
   
   ```json
   {
       "refresh": "<refresh_token>",
       "access": "<access_token>"
   }
   ```

   Ответ (ошибка)

   ```json
   {
    "error": "Неверный логин или пароль."
   }
   ```

- Получение курсов обмена
  
   URL: /api/currency/exchange_rates/
   Метод: GET
   Authorization: Bearer your_access_token_here

  Ответ (успех):
   
  ```json
  {
    "USD": {
        "Value": 100.0,
        "Nominal": 1
    },
    "EUR": {
        "Value": 120.0,
        "Nominal": 1
    },
    "RUB": {
        "Value": 1.0,
        "Nominal": 1
    }
  }
  ```

- Конвертация валюты

   URL: /api/currency/convert/
   Метод: POST
   Authorization: Bearer your_access_token_here
   Content-Type: application/json
   Тело запроса:
   
  ```json
  {
    "amount": 100,
    "from_currency": "USD",
    "to_currency": "EUR"
  }
  ```
   
   Ответ (успешно):
   
  ```json
  {
    "converted_amount": 85.0,
    "from_currency": "USD",
    "to_currency": "EUR"
   }
  ```

  Ответ (ошибка):

  ```json
   {
    "error": "Недопустимые валюты."
   }
  ```

---
