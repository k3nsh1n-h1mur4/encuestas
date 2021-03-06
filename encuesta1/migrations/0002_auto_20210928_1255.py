# Generated by Django 3.2.7 on 2021-09-28 17:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuesta1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='encuestamodel',
            name='cuarta',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='encuestamodel',
            name='primera',
            field=models.CharField(choices=[('SI', 'Si'), ('CUANTOS', 'Cuantos'), ('NO', 'No')], default='SI', max_length=10),
        ),
        migrations.AddField(
            model_name='encuestamodel',
            name='quinta',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='encuestamodel',
            name='segunda',
            field=models.CharField(choices=[('SI', 'Si'), ('NO', 'No')], default='SI', max_length=4),
        ),
        migrations.AddField(
            model_name='encuestamodel',
            name='septima',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='encuestamodel',
            name='sexta',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='encuestamodel',
            name='tercera',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='encuestamodel',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 28, 12, 55, 29, 236064)),
        ),
    ]
