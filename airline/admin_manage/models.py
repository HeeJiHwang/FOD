# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    no = models.AutoField(primary_key=True)
    id = models.CharField(max_length=20)
    pw = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    d_no = models.ForeignKey('Departments', models.DO_NOTHING, db_column='d_no')
    email = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'admin'


class AircraftType(models.Model):
    no = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=20)
    seats = models.IntegerField()
    mfr = models.CharField(max_length=20)
    seat_row = models.CharField(max_length=10)
    seat_column = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'aircraft_type'


class Airports(models.Model):
    no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)
    code = models.CharField(max_length=10)
    gate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'airports'


class Departments(models.Model):
    no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'departments'


class FlightSchedule(models.Model):
    no = models.CharField(primary_key=True, max_length=20)
    at_no = models.ForeignKey(AircraftType, models.DO_NOTHING, db_column='at_no')
    route_no = models.ForeignKey('Route', models.DO_NOTHING, db_column='route_no')
    departure_date = models.DateField()
    arrival_date = models.DateField()
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    remain_seats = models.IntegerField()
    gate_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'flight_schedule'


class Inform(models.Model):
    no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    a_no = models.ForeignKey(Admin, models.DO_NOTHING, db_column='a_no')
    ic_no = models.ForeignKey('InformCategory', models.DO_NOTHING, db_column='ic_no')
    content = models.TextField()
    date = models.DateField(blank=True, null=True ,auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'inform'


class InformCategory(models.Model):
    no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'inform_category'


class Member(models.Model):
    no = models.CharField(primary_key=True, max_length=8)
    last_name = models.CharField(max_length=10)
    first_name = models.CharField(max_length=10)
    id = models.CharField(max_length=20)
    pw = models.CharField(max_length=30)
    gender = models.IntegerField()
    birth_date = models.DateField()
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    security1 = models.CharField(max_length=10, blank=True, null=True)
    security2 = models.CharField(max_length=10, blank=True, null=True)
    sms = models.IntegerField()
    country_code = models.IntegerField()
    check_foreign = models.IntegerField(default=0)
    passport = models.CharField(max_length=30, blank=True, null=True)
    p_points = models.IntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'member'


class PassengerForm(models.Model):
    no = models.AutoField(primary_key=True)
    re_idx = models.ForeignKey('Reservation', models.DO_NOTHING, db_column='re_idx')
    seat = models.CharField(max_length=10, blank=True, null=True)
    check_in = models.IntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'passenger_form'


class PassengerInfo(models.Model):
    no = models.AutoField(primary_key=True)
    info_collect = models.IntegerField()
    nationality = models.IntegerField()
    rule_agree = models.IntegerField()
    danger_agree = models.IntegerField()
    m_no = models.ForeignKey(Member, models.DO_NOTHING, db_column='m_no')

    class Meta:
        managed = False
        db_table = 'passenger_info'


class Points(models.Model):
    no = models.AutoField(primary_key=True)
    m_no = models.ForeignKey(Member, models.DO_NOTHING, db_column='m_no')
    r_amount = models.ForeignKey('Route', models.DO_NOTHING, db_column='r_amount' , related_name='r_amount')
    r_mileage = models.ForeignKey('Route', models.DO_NOTHING, db_column='r_mileage', related_name='r_mileage')

    class Meta:
        managed = False
        db_table = 'points'


class Qna(models.Model):
    no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    qc_no = models.ForeignKey('QnaCategory', models.DO_NOTHING, db_column='qc_no')
    m_no = models.ForeignKey(Member, models.DO_NOTHING, db_column='m_no')
    date = models.DateField(blank=True, null=True, auto_now_add=True)
    answer = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qna'


class QnaCategory(models.Model):
    no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'qna_category'


class Reservation(models.Model):
    idx = models.AutoField(primary_key=True)
    re_no = models.CharField(max_length=20, blank=True, null=True)
    m_no = models.ForeignKey(Member, models.DO_NOTHING, db_column='m_no', blank=True, null=True)
    flight_no = models.CharField(max_length=20)
    f_no = models.ForeignKey(FlightSchedule, models.DO_NOTHING, db_column='f_no')
    fare_type = models.IntegerField()
    baggage_check = models.IntegerField()
    t_no = models.ForeignKey('Transaction', models.DO_NOTHING, db_column='t_no')

    class Meta:
        managed = False
        db_table = 'reservation'


class Route(models.Model):
    no = models.AutoField(primary_key=True)
    departure = models.ForeignKey(Airports, models.DO_NOTHING, db_column='departure' , related_name='departure')
    arrival = models.ForeignKey(Airports, models.DO_NOTHING, db_column='arrival', related_name='arrival')
    code = models.CharField(max_length=20)
    amount = models.IntegerField()
    mileage = models.IntegerField()
    points = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'route'


class Transaction(models.Model):
    no = models.CharField(primary_key=True, max_length=20)
    method = models.IntegerField()
    card_number = models.CharField(max_length=20, blank=True, null=True)
    account_number = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateField(blank=True, null=True,auto_now_add=True)
    pi_no = models.ForeignKey(PassengerInfo, models.DO_NOTHING, db_column='pi_no')
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'transaction'
