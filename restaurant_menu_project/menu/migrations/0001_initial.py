# Generated by Django 2.2.3 on 2019-07-24 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.CharField(max_length=200, verbose_name='Dish')),
                ('price', models.FloatField(verbose_name='Price, USD')),
            ],
        ),
    ]
