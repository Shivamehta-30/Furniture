# Generated by Django 3.2.5 on 2021-07-19 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productout', '0003_auto_20210713_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='prodoutward',
            name='cgst',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
    ]
