# Generated by Django 2.0.13 on 2019-05-18 04:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190514_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cpassword',
            field=models.CharField(default='tmp', error_messages={'unique': 'パスワードが規則に従っていません'}, help_text='aaa', max_length=150, validators=[django.core.validators.MinLengthValidator(8)], verbose_name='確認用パスワード'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(error_messages={'unique': 'パスワードが規則に従っていません'}, help_text='aaa', max_length=150, validators=[django.core.validators.MinLengthValidator(8)], verbose_name='password'),
        ),
    ]