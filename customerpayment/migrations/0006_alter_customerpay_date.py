# Generated by Django 3.2.5 on 2021-07-15 14:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerpayment', '0005_alter_customerpay_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerpay',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 15, 14, 34, 28, 883784)),
        ),
    ]
