# Generated by Django 5.1 on 2024-08-08 09:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='location',
            name='longitude',
        ),
        migrations.AddField(
            model_name='location',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=14, max_digits=20, null=True, verbose_name='Широта'),
        ),
        migrations.AddField(
            model_name='location',
            name='lng',
            field=models.DecimalField(blank=True, decimal_places=14, max_digits=20, null=True, verbose_name='Долгота'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Изображение')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.location')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
