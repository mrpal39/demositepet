# Generated by Django 3.2.7 on 2021-11-06 10:02

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='category',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
