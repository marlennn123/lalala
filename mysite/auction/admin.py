from django.contrib import admin
from .models import UserProfile, Category, CarMake, Model, Car, Bet, Comment

admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(CarMake)
admin.site.register(Model)
admin.site.register(Car)
admin.site.register(Bet)
admin.site.register(Comment)
