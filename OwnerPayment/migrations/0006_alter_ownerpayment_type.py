# Generated by Django 3.2.5 on 2021-07-04 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OwnerPayment', '0005_alter_ownerpayment_cash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownerpayment',
            name='type',
            field=models.CharField(choices=[('cash', 'cash'), ('netbank', 'netbank'), ('upi', 'upi'), ('cheque', 'cheque')], max_length=80),
        ),
    ]
