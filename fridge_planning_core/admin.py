from django.contrib import admin

from .models import Foodstuff, Recipe, Fridge, Ingredient, Supply, Meal


admin.site.register(Foodstuff)
admin.site.register(Recipe)
admin.site.register(Fridge)
admin.site.register(Ingredient)
admin.site.register(Supply)
admin.site.register(Meal)
