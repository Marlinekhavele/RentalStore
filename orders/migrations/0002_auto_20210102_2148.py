# Generated by Django 3.0.7 on 2021-01-02 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='price',
            new_name='price_per_book',
        ),
    ]