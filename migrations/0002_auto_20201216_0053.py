# Generated by Django 3.1.3 on 2020-12-16 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(default='1234', max_length=30),
        ),
        migrations.AddField(
            model_name='users',
            name='role_id',
            field=models.CharField(choices=[('1', 'Admin'), ('2', 'Moderator'), ('3', 'User')], default='3', max_length=1),
        ),
    ]
