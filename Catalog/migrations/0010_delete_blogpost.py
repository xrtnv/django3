# Generated by Django 5.0.5 on 2024-06-18 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0009_product_owner'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]