# Generated by Django 3.0.2 on 2020-01-19 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toilets', '0019_auto_20200119_1543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toilet',
            name='remarks',
        ),
    ]
