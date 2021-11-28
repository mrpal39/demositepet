# Generated by Django 3.2.7 on 2021-11-06 00:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('kennels', '0002_alter_kennel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kennel',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]