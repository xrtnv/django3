# Generated by Django 5.0.5 on 2024-05-07 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='manufactured_at',
            field=models.DateTimeField(blank=True, help_text='Введите дату производства', null=True, verbose_name='Дата производства'),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
