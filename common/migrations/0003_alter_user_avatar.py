# Generated by Django 4.1.1 on 2022-09-17 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='profile/default.jpg', upload_to='profile/'),
        ),
    ]
