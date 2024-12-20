# Generated by Django 5.0 on 2024-12-19 06:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Invoice_App', '0003_alter_invoiceproduct_table'),
        ('User_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='invoices', to='User_App.user'),
        ),
    ]