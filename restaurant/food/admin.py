from django.contrib import admin
from restaurant.food.models import Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = 'name address'.split()
    ordering = ('name',)
