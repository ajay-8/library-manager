# Generated by Django 5.0.4 on 2024-04-20 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookcheckoutinfo',
            options={'verbose_name_plural': 'Book Checkout Details'},
        ),
        migrations.AlterModelTable(
            name='bookcheckoutinfo',
            table='BookCheckoutInfo',
        ),
    ]
