# Generated by Django 3.2.7 on 2021-10-16 03:25

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import pet.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(default="It is black and chubby, very shy, has went gone next to the school in downtown. There's a slight flaw in the tail fur.", max_length=500)),
                ('size', models.CharField(blank=True, choices=[('SM', 'Small'), ('MD', 'Medium'), ('LG', 'Large')], max_length=2)),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('sex', models.CharField(blank=True, choices=[('FE', 'Female'), ('MA', 'Male')], max_length=2)),
                ('profile_picture', models.ImageField(help_text='Maximum image size is 8MB', upload_to='pet_profiles')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=pet.models.get_slug)),
                ('breeds', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pet.bread')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pet.category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities.state')),
            ],
            options={
                'ordering': ['-id'],
                'unique_together': {('name', 'owner')},
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pet_photos')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pet.pet')),
            ],
        ),
        migrations.AddField(
            model_name='bread',
            name='Category',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Category', to='pet.category'),
        ),
    ]
