# Generated by Django 3.2.7 on 2021-12-18 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0004_auto_20211218_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
