# Generated by Django 3.0.2 on 2020-01-16 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toilets', '0002_auto_20200116_1340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toilet',
            name='accessible',
        ),
        migrations.RemoveField(
            model_name='toilet',
            name='clean',
        ),
    ]