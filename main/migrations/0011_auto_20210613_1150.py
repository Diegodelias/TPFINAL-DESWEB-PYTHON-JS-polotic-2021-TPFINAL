# Generated by Django 3.2.4 on 2021-06-13 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_carrito_titulo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrito',
            name='producto',
        ),
        migrations.AddField(
            model_name='carrito',
            name='productos',
            field=models.ManyToManyField(to='main.Producto'),
        ),
    ]