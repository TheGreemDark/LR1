### API Управления Пользователями

Данное REST API построено с применением Litestar и SQLAlchemy и предназначено для управления данными пользователей.

### Установка и запуск

1. Создайте и активируйте виртуальное окружение

python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate # Linux/Mac
3. Установите зависимости

pip install litestar sqlalchemy aiosqlite pydantic
3. Инициализируйте базу данных

python init_db.py
4. Запустите приложение

python -m app.main
По умолчанию сервер доступен по адресу http://127.0.0.1:8000 (адрес 0.0.0.0 не подходит для этого приложения).

### Проверка API

В каталоге crud_examples содержатся примеры скриптов для всех CRUD операций с подробным описанием:

- get_operations.py — запросы на получение данных (список пользователей, пользователь по ID)
- post_operations.py — создание пользователя, обработка ошибок
- put_operations.py — обновление данных полностью или частично
- delete_operations.py — удаление пользователя и проверка результата

### Перед запуском убедитесь, что:

- Сервер запущен (python -m app.main)
- База данных инициализирована (python init_db.py)
- Установлен пакет requests (pip install requests)

Доступные API endpoints
### Получение пользователя по ID

- Метод: GET
- URL: http://127.0.0.1:8000/users/{user_id}
- Возвращает данные конкретного пользователя

### Создание пользователя

- Метод: POST
- URL: http://127.0.0.1:8000/users
- Пример тела запроса:
  
JSON
{
    "username": "Loken_X",
    "email": "Loken_X_Istvaan_III@example.com",
    "full_name": "Локен Хорусович"
}
### Обновление пользователя

- Метод: PUT
- URL: http://127.0.0.1:8000/users/{user_id}
- Пример тела запроса:

JSON


{
    "username": "Cerberus_updated",
    "email": "Cerberus.new_Out@example.com",
    "full_name": "Церберус Новый как с завода"
}
### Для работы с API можно использовать инструменты, такие как Postman, curl или Python-скрипты из папки примеров.
- Метод: DELETE
- URL: http://127.0.0.1:8000/users/{user_id}
- Описание

### Удаляет пользователя с указанным ID из базы данных

- Как использовать
- 
Oтправьте DELETE-запрос на указанный URL с нужным ID пользователя

### Тестирование API
## 1. Использование curl (Windows PowerShell)

- Получение всех пользователей

curl http://127.0.0.1:8000/users

- Получение пользователя по ID (пример ID=1)

curl http://127.0.0.1:8000/users/1

- Создание нового пользователя

$body = @{
    username = "Loken_X"
    email = "Loken_X_Istvaan_III@example.com"
    full_name = "Локен Хорусович"
} | ConvertTo-Json

curl -X POST http://127.0.0.1:8000/users `
     -H "Content-Type: application/json" `
     -d $body

- Обновление пользователя (пример ID=1)

$body = @{
    username = "Cerberus_updated"
    email = "Cerberus.new_Out@example.com"
    full_name = "Церберус Новый как с завода"
} | ConvertTo-Json

curl -X PUT http://127.0.0.1:8000/users/1 `
     -H "Content-Type: application/json" `
     -d $body

- Удаление пользователя (пример ID=1)

curl -X DELETE http://127.0.0.1:8000/users/1
Для Linux/Mac в командах curl вместо обратного апострофа (`) используйте обратный слэш () для переноса строк, например:

curl -X POST http://127.0.0.1:8000/users \
     -H "Content-Type: application/json" \
     -d '{"username": "Loken_X", "email": "Loken_X_Istvaan_III@example.com", "full_name": "Локен Хорусович"}'

## 2. Использование Postman

- Скачайте и установите Postman: 
- Создайте новый запрос, выберите HTTP-метод (GET, POST, PUT, DELETE)
- Введите URL для нужной операции
- Для POST и PUT добавьте тело запроса в формате JSON во вкладке "Body"
- Нажмите кнопку "Send" для отправки запроса и просмотра ответа

## 3. Использование браузера

- GET-запросы (получение данных) можно выполнять напрямую из адресной строки браузера
- Для POST, PUT, DELETE необходимы инструменты, такие как Postman, curl или расширения браузера

Файл parsed_tasks.json не относится к данному руководству и не используется.
