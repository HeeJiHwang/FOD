# Generated by Django 3.1.3 on 2022-09-13 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.DeleteModel(
            name='AircraftType',
        ),
        migrations.DeleteModel(
            name='Airports',
        ),
        migrations.DeleteModel(
            name='Departments',
        ),
        migrations.DeleteModel(
            name='FlightSchedule',
        ),
        migrations.DeleteModel(
            name='Inform',
        ),
        migrations.DeleteModel(
            name='InformCategory',
        ),
        migrations.DeleteModel(
            name='Member',
        ),
        migrations.DeleteModel(
            name='PassengerForm',
        ),
        migrations.DeleteModel(
            name='PassengerInfo',
        ),
        migrations.DeleteModel(
            name='Points',
        ),
        migrations.DeleteModel(
            name='Qna',
        ),
        migrations.DeleteModel(
            name='QnaCategory',
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
        migrations.DeleteModel(
            name='Route',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]