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
# прежде чем создавать машины, оставлять комееты и т.д. за логинтесь через админку. Если нужно сменить акаунт разлгинивайтесь и логинтесь через админку

