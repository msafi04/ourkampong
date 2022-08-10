# Generated by Django 3.0.4 on 2022-08-03 06:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('item', '0005_auto_20220802_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='donate_badge',
            field=models.ManyToManyField(related_name='Donate_Badge', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='item',
            name='share_badge',
            field=models.ManyToManyField(related_name='Share_Badge', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(blank=True, choices=[('New', 'New'), ('Old', 'Old'), ('Used', 'Used'), ('Unused', 'Unused'), ('Damaged', 'Damaged')], max_length=7, null=True, verbose_name='Labels'),
        ),
    ]
