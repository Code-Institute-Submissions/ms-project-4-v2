# Generated by Django 3.2 on 2022-05-17 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default='No Description', max_length=254),
        ),
    ]
