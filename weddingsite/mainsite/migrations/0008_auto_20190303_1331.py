# Generated by Django 2.1.2 on 2019-03-03 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0007_auto_20190303_1324'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guest',
            options={'ordering': ['id', 'has_presence', 'name']},
        ),
        migrations.AlterField(
            model_name='guest',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]