# Generated by Django 3.0.5 on 2020-05-24 06:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BistroManagementToolApp', '0002_transaction_products_in_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now, null=True),
        ),
    ]
