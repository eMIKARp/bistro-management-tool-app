# Generated by Django 3.0.5 on 2020-05-24 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BistroManagementToolApp', '0003_auto_20200524_0623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='netto_transaction_value_23_VAT',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='netto_transaction_value_5_VAT',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='netto_transaction_value_8_VAT',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='payment_type',
            field=models.CharField(choices=[('CASH', 'CASH'), ('CARD', 'CARD')], default='CASH', max_length=4),
        ),
    ]
