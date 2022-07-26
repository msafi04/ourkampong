# Generated by Django 3.0.4 on 2022-07-26 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='cat_slug',
            field=models.SlugField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(choices=[('TO', 'Toys'), ('AP', 'Apparels'), ('BO', 'Books'), ('ST', 'Stationery'), ('FU', 'Furniture'), ('HW', 'Hardwares'), ('SN', 'Snacks'), ('EL', 'Electronis'), ('HI', 'Household_Items'), ('SP', 'Sports'), ('OT', 'Others')], max_length=2, verbose_name='Categories'),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('TO', 'Toys'), ('AP', 'Apparels'), ('BO', 'Books'), ('ST', 'Stationery'), ('FU', 'Furniture'), ('HW', 'Hardwares'), ('SN', 'Snacks'), ('EL', 'Electronis'), ('HI', 'Household_Items'), ('SP', 'Sports'), ('OT', 'Others')], max_length=2, verbose_name='Categories'),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('NW', 'New'), ('OL', 'Old'), ('US', 'Used'), ('UN', 'Unused'), ('DM', 'Damaged')], max_length=2, verbose_name='Labels'),
        ),
    ]