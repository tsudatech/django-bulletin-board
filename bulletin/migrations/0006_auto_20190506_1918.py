# Generated by Django 2.0.13 on 2019-05-06 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0005_auto_20190506_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='access',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
