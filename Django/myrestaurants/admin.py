from django.contrib import admin
from myrestaurants import models

admin.site.register(models.Restaurant)
admin.site.register(models.Dish)
