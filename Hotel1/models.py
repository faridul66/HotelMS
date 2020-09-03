from django.db import models
from django.utils import timezone


class AddCustomer(models.Model):
    first = models.CharField(max_length=20)
    sur = models.CharField(max_length=20)
    last = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.IntegerField()
    gender = models.CharField(max_length=20)
    date = models.DateTimeField(default=timezone.now)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.first


class AddRoom(models.Model):
    r_number = models.IntegerField()
    r_cost = models.IntegerField()
    r_type = models.CharField(max_length=20)
    r_description = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.r_type


class RoomBooking(models.Model):
    name = models.CharField(max_length=20)
    r_number = models.IntegerField()
    phone = models.IntegerField()
    from_date = models.DateTimeField(default=timezone.now)
    to_date = models.DateTimeField(default=timezone.now)
    amount = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class LoundryBooking(models.Model):
    r_number = models.CharField(max_length=20)
    date = models.DateTimeField(default=timezone.now)
    r_cost = models.IntegerField()
    r_description = models.TextField()

    def __str__(self):
        return self.r_number


class Cleaning(models.Model):
    r_number = models.CharField(max_length=20)
    r_description = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.r_description




