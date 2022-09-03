from django.contrib import admin
from .models import Hotel, Room, Guest, Reservation, Cleaning
from datetime import datetime

# Register your models here.
@admin.register(Hotel)
class Hotel_Admin(admin.ModelAdmin):
    list_display = ['name_hotel', 'number_phone', 'adress', 'town']
    list_editable = ['number_phone', 'adress', 'town']


@admin.register(Room)
class Hotel_Admin(admin.ModelAdmin):
    list_display = ['number_hotel', 'active', 'square_room', 'vol_room', 'floor', 'max_quests']
    list_editable = ['active', 'square_room', 'vol_room']


@admin.register(Guest)
class Guest_Admin(admin.ModelAdmin):
    list_display = ['name', 'lastname', 'number_phone', 'id_passport', 'e_mail', 'country']


@admin.register(Reservation)
class Reservation_Admin(admin.ModelAdmin):
    list_display = ['number_kvartira', 'vol_guest', 'status', 'e_mail', 'date_create', 'date_check_in',
                    'date_check_out', 'vol_day', 'notes']
    list_editable = ['status']


    def vol_day(self, reservation):
        result = str(reservation.date_check_out - reservation.date_check_in)[:6]
        return result


@admin.register(Cleaning)
class Cleaning_Admin(admin.ModelAdmin):
    list_display = ['name', 'lastname', 'number_phone']


class Schedule_Admin(admin.ModelAdmin):
    list_display = ['name', 'lastname', 'number_phone']