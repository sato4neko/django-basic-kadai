# Generated by Django 5.1.1 on 2024-09-23 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0009_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
