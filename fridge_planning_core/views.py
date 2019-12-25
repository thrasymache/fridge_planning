from django.shortcuts import render
from django.http import HttpResponse
from .models import Ingredient, Meal, Supply

def calendar(request):
    available = {
            s.foodstuff: s.quantity
            for s in Supply.objects.all()
    }
    print(available)
    for meal in Meal.objects.order_by('date'):
        for ing in meal.recipe.ingredient_set.all():
            if ing.foodstuff in available:
                available[ing.foodstuff] -= ing.quantity
            else:
                available[ing.foodstuff] = -ing.quantity
            print(ing.foodstuff, available[ing.foodstuff])
    print(available)
    context = {
        'meals': Meal.objects.all(),
        'missing_ingredients': {f: -q for f,q in available.items() if q < 0},
        'excess_ingredients':  {f: q for f,q in available.items() if q > 0},
    }
    return render(request, 'calendar.html', context)
