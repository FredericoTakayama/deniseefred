# Generated by Django 2.1.2 on 2019-03-10 16:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='last_update',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AddField(
            model_name='guest',
            name='message',
            field=models.TextField(help_text='Deixe aqui sua mensagem aos noivos', null=True),
        ),
        migrations.AddField(
            model_name='guest',
            name='password',
            field=models.CharField(default='43d11419', max_length=9),
        ),
    ]
