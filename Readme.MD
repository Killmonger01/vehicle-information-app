# vehicle-information-app
# Как запустить локально
- создайте и активируйте вертуальное окружение
```
python -m venv venv
source venv/Scripts/activate # Для Windows
source venv/bin/activate # Для MacOS, Linux
```
- Обновите pip и установите зависимости
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
- перейдите в директерию с manage.py 
```
cd vehicle
```
- Сделайте миграции
```
python manage.py makemigrations
python manage.py migrate
```
- Создайте суперпользователя и запустите сервер
```
python manage.py createsuperuser
python manage.py runserver
```
- прежде чем создавать машины, оставлять коменты и т.д. за логинтесь через админку. Если нужно сменить акаунт разлгинивайтесь и логинтесь через админку
- что бы использовать api получите access token по этому эндпоинту http://127.0.0.1:8000/api/token/  {"username": "your_username",  "password": "your_password"}
# Список эндпоинтов
- GET /api/cars/ — получение списка автомобилей.
- GET /api/cars/<id>/ — получение информации о конкретном автомобиле.
- POST /api/cars/ — создание нового автомобиля.
- PUT /api/cars/<id>/ — обновление информации о автомобиле.
- DELETE /api/cars/<id>/ — удаление автомобиля.
- GET /api/cars/<id>/comments/ — получение комментариев к автомобилю.
- POST /api/cars/<id>/comments/ — добавление нового комментария к автомобилю.
