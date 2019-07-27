# Generated by Django 2.2.3 on 2019-07-24 23:52

from django.db import migrations


def create_data(apps, schema_editor):
    Menu = apps.get_model('menu', 'Menu')
    Menu(dish='FISH&CHIPS SHARK AND SWEET POTATOES', price='3.45').save()
    Menu(dish='RICE WITH CHICKEN', price='2.7').save()
    Menu(dish='BOWL WITH AVOCADO AND TUNA', price='3.3').save()
    Menu(dish='TOAST WITH AVOCADO AND CHIA', price='1.75').save()
    Menu(dish='FRESH SALAD WITH SHARK SASHIMI', price='4.15').save()
    Menu(dish='WILD SCALLOP', price='8.9').save()
    Menu(dish='MARLIN STEAK', price='15.5').save()
    Menu(dish='WARM CHINESE SALAD WITH VEAL & EGGPLANT', price='6.45').save()


class Migration(migrations.Migration):
    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]
