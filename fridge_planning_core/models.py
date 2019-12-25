from django.db import models


class Foodstuff(models.Model):
    common_name = models.CharField(max_length=100)
    units = models.CharField(max_length=30)

    def __str__(self):
        return self.common_name


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Fridge(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    foodstuff = models.ForeignKey(Foodstuff, on_delete=models.PROTECT)
    quantity = models.IntegerField()

    def __str__(self):
        return "%s - %s" % (self.recipe.title, self.foodstuff.common_name)


class Supply(models.Model):
    foodstuff = models.ForeignKey(Foodstuff, on_delete=models.PROTECT)
    fridge = models.ForeignKey(Fridge, on_delete=models.PROTECT)
    quantity = models.IntegerField()

    def __str__(self):
        return "%d  %s of %s" % (
                self.quantity,
                self.foodstuff.units,
                self.foodstuff.common_name)

class Meal(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.PROTECT)
    date = models.DateField()

    def __str__(self):
        return "%s - %s" % (self.date, self.recipe.title)
