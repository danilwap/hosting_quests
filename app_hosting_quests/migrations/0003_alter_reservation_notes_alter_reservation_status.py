# Generated by Django 4.0.6 on 2022-09-03 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_hosting_quests', '0002_reservation_rename_squere_room_room_square_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='notes',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(blank=True, choices=[('З', 'ЗАПРОС'), ('П', 'Подтверждено'), ('О', 'ОТМЕНА')], max_length=1),
        ),
    ]
