# Generated by Django 2.1.2 on 2019-03-03 16:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0008_auto_20190303_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular guest', primary_key=True, serialize=False),
        ),
    ]
