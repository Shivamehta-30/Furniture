# Generated by Django 3.2.5 on 2021-07-19 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outward_purchase', '0002_auto_20210713_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='outward_purchase',
            name='cgst',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
    ]
