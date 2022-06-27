from django.db import models

# Create your models here.

from django.db import models

# Create your models here.


class Region(models.Model):
    regionName = models.CharField(max_length=50)

    def __str__(self):
        return self.regionName


class Parameter(models.Model):
    parameter_name = models.CharField(max_length=50)
    region = models.ForeignKey(
        Region, related_name='parameter', on_delete=models.CASCADE)

    def __str__(self):
        return self.parameter_name


class YearTemperature(models.Model):
    parameter = models.ForeignKey(
        Parameter, related_name='yeartemperature', on_delete=models.CASCADE)
    year = models.CharField(max_length=10)
    win = models.FloatField(null=True)
    spr = models.FloatField(null=True)
    sum = models.FloatField(null=True)
    aut = models.FloatField(null=True)
    ann = models.FloatField(null=True)

    def __str__(self):
        return self.year


class MonthTemperature(models.Model):
    year = models.ForeignKey(
        YearTemperature, related_name='monthtemperature', on_delete=models.CASCADE)
    month = models.CharField(max_length=20)
    temperature = models.FloatField(null=True)

    def __str__(self):
        return self.month
