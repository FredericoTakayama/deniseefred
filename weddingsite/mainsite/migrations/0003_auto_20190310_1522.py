# Generated by Django 2.1.2 on 2019-03-10 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_auto_20190310_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='password',
            field=models.CharField(default='6c528006', max_length=9),
        ),
    ]
