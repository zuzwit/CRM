# Generated by Django 3.1.3 on 2020-12-16 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20201216_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]