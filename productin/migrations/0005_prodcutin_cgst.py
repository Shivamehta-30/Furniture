# Generated by Django 3.2.5 on 2021-07-19 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productin', '0004_alter_prodcutin_qun'),
    ]

    operations = [
        migrations.AddField(
            model_name='prodcutin',
            name='cgst',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
    ]
