# Generated by Django 3.2.9 on 2021-12-06 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0015_auto_20211205_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='empl_id',
            field=models.CharField(default='0000', max_length=4),
        ),
    ]
