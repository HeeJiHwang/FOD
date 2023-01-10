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
    d_no = models.ForeignKey('Departments', db_column='d_no', on_delete=models.CASCADE)
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
    at_no = models.ForeignKey(AircraftType, db_column='at_no', on_delete=models.CASCADE)
    route_no = models.ForeignKey('Route', db_column='route_no', on_delete=models.CASCADE)
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
    a_no = models.ForeignKey(Admin, db_column='a_no', on_delete=models.CASCADE)
    ic_no = models.ForeignKey('InformCategory', db_column='ic_no', on_delete=models.CASCADE)
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
    re_idx = models.ForeignKey('Reservation', db_column='re_idx', on_delete=models.CASCADE)
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
    m_no = models.ForeignKey(Member, db_column='m_no', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'passenger_info'


class Points(models.Model):
    no = models.AutoField(primary_key=True)
    m_no = models.ForeignKey(Member, db_column='m_no', on_delete=models.CASCADE)
    r_amount = models.ForeignKey('Route', db_column='r_amount' , related_name='r_amount', on_delete=models.CASCADE)
    r_mileage = models.ForeignKey('Route', db_column='r_mileage', related_name='r_mileage', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'points'


class Qna(models.Model):
    no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    qc_no = models.ForeignKey('QnaCategory', db_column='qc_no', on_delete=models.CASCADE)
    m_no = models.ForeignKey(Member, db_column='m_no', on_delete=models.CASCADE)
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
    m_no = models.ForeignKey(Member, db_column='m_no', blank=True, null=True, on_delete=models.CASCADE)
    flight_no = models.CharField(max_length=20)
    f_no = models.ForeignKey(FlightSchedule, db_column='f_no', on_delete=models.CASCADE)
    fare_type = models.IntegerField()
    baggage_check = models.IntegerField()
    t_no = models.ForeignKey('Transaction', db_column='t_no', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'reservation'


class Route(models.Model):
    no = models.AutoField(primary_key=True)
    departure = models.ForeignKey(Airports, db_column='departure' , related_name='departure', on_delete=models.CASCADE)
    arrival = models.ForeignKey(Airports, db_column='arrival', related_name='arrival', on_delete=models.CASCADE)
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
    pi_no = models.ForeignKey(PassengerInfo, db_column='pi_no', on_delete=models.CASCADE)
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'transaction'