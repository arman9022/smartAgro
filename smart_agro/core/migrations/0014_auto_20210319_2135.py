# Generated by Django 3.1.5 on 2021-03-19 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_farmer_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='address',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
