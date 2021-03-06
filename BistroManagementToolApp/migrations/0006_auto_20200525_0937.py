# Generated by Django 3.0.5 on 2020-05-25 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BistroManagementToolApp', '0005_auto_20200524_0757'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='number_of_products_in_transaction',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=10),
        ),
        migrations.AlterField(
            model_name='productsintransaction',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_in_transaction', to='BistroManagementToolApp.Product'),
        ),
        migrations.AlterField(
            model_name='productsintransaction',
            name='quantity',
            field=models.DecimalField(blank=True, decimal_places=2, default='0.00', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='productsintransaction',
            name='transaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to='BistroManagementToolApp.Transaction'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='sales_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transactions', to='BistroManagementToolApp.ApplicationUser'),
        ),
    ]
