# Generated by Django 3.0.8 on 2020-08-22 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='game',
            field=models.CharField(max_length=50, verbose_name='نام بازی'),
        ),
        migrations.AlterField(
            model_name='score',
            name='loser',
            field=models.CharField(max_length=50, verbose_name='نام بازنده'),
        ),
        migrations.AlterField(
            model_name='score',
            name='winner',
            field=models.CharField(max_length=50, verbose_name='نام برنده'),
        ),
    ]
