# Generated by Django 3.2.4 on 2021-06-23 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_rename_quantity_itemcarrito_cantidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='total',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
