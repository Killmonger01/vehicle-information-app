from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()
# Модель автомобиля
class Car(models.Model):
    make = models.CharField(max_length=100)  # Марка автомобиля
    model = models.CharField(max_length=100)  # Модель автомобиля
    year = models.IntegerField()  # Год выпуска
    description = models.TextField(blank=True, null=True)  # Описание автомобиля
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания записи
    updated_at = models.DateTimeField(auto_now=True)  # Дата последнего обновления записи
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # Владелец записи (пользователь)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"


# Модель комментария
class Comment(models.Model):
    content = models.TextField()  # Содержание комментария
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания комментария
    car = models.ForeignKey(Car, related_name='comments', on_delete=models.CASCADE)  # Связь с автомобилем
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Автор комментария

    def __str__(self):
        return f"Comment by {self.author} on {self.car}"
