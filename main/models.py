from __future__ import unicode_literals

from django.db import models


# Create your models here.

class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.email


class GS(models.Model):
    isin = models.CharField(max_length=12)
    return_rate = models.FloatField()
    date_of_issue = models.DateField()
    date_of_maturity = models.DateField()
    outstanding_stock = models.FloatField()

    def __str__(self):
        return self.isin


class Goal(models.Model):
    # TODO: Add more goal choices
    GOAL_CHOICES = (
        ('car', 'car'),
        ('house', 'house'),
    )

    user = models.ForeignKey(User, on_delete='CASCADE')
    _type = models.CharField(choices=GOAL_CHOICES, max_length=30)
    amount = models.FloatField()
    target_date = models.DateField()

    def __str__(self):
        return self._type + " goal for " + self.user.email
