# Generated by Django 4.1.1 on 2022-09-17 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='default.jpg', upload_to='profile/'),
        ),
    ]
