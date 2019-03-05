# Generated by Django 2.1.2 on 2019-03-03 15:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_auto_20190106_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular guest', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='guest',
            name='invited_by',
            field=models.CharField(choices=[('m', 'noivo'), ('f', 'noiva')], max_length=2, verbose_name='Convidado pelo(a)'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='num_of_babies',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1, help_text='Número de crianças até 5 anos', verbose_name='Número de bebes'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='num_of_children',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1, help_text='Número de crianças entre 6 e 10 anos', verbose_name='Número de crianças'),
        ),
    ]
