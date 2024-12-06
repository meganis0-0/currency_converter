# Currency Converter App

## Описание

Это приложение позволяет пользователям конвертировать валюту с использованием актуальных курсов валют. Пользователи могут зарегистрироваться, войти в систему и выполнять конвертацию валюты.

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
     ![image](https://github.com/user-attachments/assets/46c4a6c4-16eb-4644-ba7e-cf211929c740)

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

