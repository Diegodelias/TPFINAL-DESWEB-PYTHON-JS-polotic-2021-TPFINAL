# Generated by Django 3.2.4 on 2021-06-23 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20210623_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='total',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='itemcarrito',
            name='quantity',
            field=models.PositiveIntegerField(default=1, null=True),
        ),
    ]