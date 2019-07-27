from django.db import models


class Menu(models.Model):
    dish = models.CharField(max_length=200, null=False, blank=False,
                            verbose_name='Dish')
    price = models.FloatField(blank=False, verbose_name='Price, USD')

    def __str__(self):
        return self.dish
