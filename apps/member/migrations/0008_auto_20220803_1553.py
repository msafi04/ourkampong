# Generated by Django 3.0.4 on 2022-08-03 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0007_auto_20220803_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='share_badge',
            field=models.PositiveIntegerField(default=10),
        ),
    ]
