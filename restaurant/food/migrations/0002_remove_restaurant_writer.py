# Generated by Django 2.2.7 on 2019-11-27 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='writer',
        ),
    ]
