# Generated by Django 2.0.13 on 2019-05-24 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_user_cpassword'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_img',
            field=models.ImageField(default=None, null=True, upload_to='mysite'),
        ),
    ]