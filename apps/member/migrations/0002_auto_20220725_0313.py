# Generated by Django 3.0.4 on 2022-07-25 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='postal_code',
            field=models.CharField(default=None, max_length=7, null=True),
        ),
    ]
