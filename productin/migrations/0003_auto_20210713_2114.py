# Generated by Django 3.2.5 on 2021-07-13 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productin', '0002_prodcutin_is_billed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prodcutin',
            name='GSTno',
            field=models.CharField(blank=True, default=0, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='prodcutin',
            name='discount',
            field=models.FloatField(blank=True, default=0, max_length=100, null=True),
        ),
    ]
