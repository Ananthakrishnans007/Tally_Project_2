# Generated by Django 4.0.6 on 2022-09-03 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_voucher_register_credit_amount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voucher_register',
            name='Vch_No',
        ),
        migrations.RemoveField(
            model_name='voucher_register',
            name='Vch_Type',
        ),
    ]