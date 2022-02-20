from django.db import models
from django import forms


class Drinks(models.Model):
    drink = models.CharField(max_length=15, verbose_name='Напитки')

    def __str__(self):
        return self.drink

class Attendance(models.Model):
    to_be = models.CharField(max_length=30, verbose_name='Присутствие')

    def __str__(self):
        return self.to_be

class WeddingData(models.Model):
    attendance = models.ForeignKey(Attendance, null=True, on_delete=models.CASCADE, verbose_name='Присутсвие')
    name = models.CharField(max_length=250, verbose_name='Имя')
    surname = models.CharField(max_length=120, verbose_name='Фамилия')
    housing = models.BooleanField(default=False, blank=False, verbose_name='Наличие жилья')
    drink = models.ManyToManyField(Drinks, blank=True, verbose_name='Предпочтения по напиткам')
    date_submit = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')

