# Generated by Django 4.1.1 on 2022-09-17 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0009_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='default.png', upload_to='profile/'),
        ),
    ]