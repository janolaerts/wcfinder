# Generated by Django 3.0.2 on 2020-01-18 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toilets', '0003_toilet_remarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='toilet',
            name='clean',
            field=models.BooleanField(default=False),
        ),
    ]
