# Generated by Django 3.0.4 on 2022-08-05 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0012_auto_20220805_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='profile_pic',
            field=models.ImageField(blank=True, default='uploads/profile/default_profile.png', null=True, upload_to='uploads/profile/'),
        ),
    ]
