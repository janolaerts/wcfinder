# Generated by Django 3.0.2 on 2020-01-19 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toilets', '0016_toilet_clean'),
    ]

    operations = [
        migrations.RenameField(
            model_name='toilet',
            old_name='clean',
            new_name='cleanliness',
        ),
    ]
