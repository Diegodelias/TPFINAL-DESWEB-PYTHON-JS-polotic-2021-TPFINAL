# Generated by Django 3.2.4 on 2021-06-23 11:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20210623_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
