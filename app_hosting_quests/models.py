from django.db import models


# Create your models here.

class Hotel(models.Model):
    name_hotel = models.CharField(max_length=40)
    number_phone = models.IntegerField()
    adress = models.CharField(max_length=40)
    town = models.CharField(max_length=50)


class Room(models.Model):
    number_hotel = models.CharField(max_length=40)
    active = models.IntegerField()
    square_room = models.IntegerField()
    vol_room = models.IntegerField()
    vol_bad = models.IntegerField()
    floor = models.IntegerField()
    max_quests = models.IntegerField()


class Guest(models.Model):
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    number_phone = models.IntegerField()
    id_passport = models.IntegerField()
    e_mail = models.EmailField()
    country = models.CharField(max_length=40)


class Reservation(models.Model):
    STATUS_CHOICES = [
        ("З", "ЗАПРОС"),
        ("П", "ПОДТВЕРЖДЕНО"),
        ("О", "ОТМЕНА"),
    ]

    number_kvartira = models.IntegerField()
    id_guest = models.IntegerField()
    vol_guest = models.IntegerField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=True)
    e_mail = models.EmailField()
    date_create = models.DateTimeField()
    date_check_in = models.DateTimeField()
    date_check_out = models.DateTimeField()
    notes = models.CharField(max_length=40, blank=True)


class Cleaning(models.Model):
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    number_phone = models.IntegerField()




'''Schedule
	Информация берется из Reservation и других сущностей, т.е отдельная таблица в бд не создается
День и месяц (Например 18 Mon)
Время (приезда или выезда, зависит от след столбца)
Событие (выезд или приезд)
Имя гостя
Количество ночей
Номер квартиры и название отеля (например Hotel Five Stars, 431)
ID резервации (плюс ссылка на саму резервацию)
Дропдаун для выбора человека на уборку'''
