# Generated by Django 3.2.4 on 2021-06-29 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='documnets',
            field=models.FileField(default='', upload_to='docs'),
        ),
        migrations.AddField(
            model_name='customer',
            name='photo',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='companyname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
