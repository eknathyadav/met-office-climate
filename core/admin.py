from django.contrib import admin

# Register your models here.
from core.models import Region, Parameter, YearTemperature, MonthTemperature

admin.site.register(Region)
admin.site.register(Parameter)
admin.site.register(YearTemperature)
admin.site.register(MonthTemperature)
