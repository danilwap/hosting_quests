from django.contrib import admin
from .models import Hotel, Room, Guest, Reservation, Cleaning, Schedule


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
    list_display = ['number_kvartira', 'vol_guest', 'status', 'e_mail', 'date_create', 'dateandtime_check_in',
                    'dateandtime_check_out', 'vol_day', 'notes']
    list_editable = ['status']

    def vol_day(self, reservation):
        result = str(reservation.dateandtime_check_in - reservation.dateandtime_check_out)[:6]
        return result


@admin.register(Cleaning)
class Cleaning_Admin(admin.ModelAdmin):
    list_display = ['name', 'lastname', 'number_phone']


@admin.register(Schedule)
class Schedule_Admin(admin.ModelAdmin):
    list_display = ['dateandtime_check_in']

    def dateandtime_check_in(self, schedule):
        result = schedule.dateandtime_check_in
        return result