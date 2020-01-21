# Generated by Django 3.0.2 on 2020-01-19 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toilets', '0013_remove_toilet_clean'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toilet',
            name='number',
            field=models.IntegerField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='toilet',
            name='reference',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]