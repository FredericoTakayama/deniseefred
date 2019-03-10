# Generated by Django 2.1.2 on 2019-03-10 18:22

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique ID for this particular guest', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Nome', max_length=50, verbose_name='Nome')),
                ('lastname', models.CharField(help_text='Sobrenome', max_length=100, verbose_name='Sobrenome')),
                ('gender', models.CharField(choices=[('m', 'Homem'), ('f', 'Mulher')], help_text='Gênero', max_length=2, verbose_name='Gênero')),
                ('address', models.TextField(blank=True, max_length=2000, null=True)),
                ('is_vip', models.BooleanField(default=False)),
                ('invited_by', models.CharField(choices=[('m', 'noivo'), ('f', 'noiva')], max_length=2, verbose_name='Convidado pelo(a)')),
                ('main_inviter', models.BooleanField(default=False)),
                ('has_presence', models.BooleanField(default=False, help_text='Confirmar Presença', verbose_name='Confirmar Presença')),
                ('max_family_quantity', models.IntegerField(default=1)),
                ('family_quantity', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1, help_text='Total de pessoas que irão junto incluindo você', verbose_name='Número de pessoas')),
                ('num_of_babies', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0, help_text='Número de crianças até 5 anos', verbose_name='Número de bebes')),
                ('num_of_children', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0, help_text='Número de crianças entre 6 e 10 anos', verbose_name='Número de crianças')),
                ('message', models.TextField(help_text='Deixe aqui sua mensagem aos noivos', null=True)),
                ('password', models.CharField(default='419f255d', max_length=9)),
                ('last_update', models.DateField(default=datetime.datetime.today)),
            ],
            options={
                'ordering': ['id', 'has_presence', 'name'],
            },
        ),
    ]
