# Generated by Django 3.0.2 on 2020-01-18 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toilets', '0004_toilet_clean'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toilet',
            name='clean',
        ),
    ]