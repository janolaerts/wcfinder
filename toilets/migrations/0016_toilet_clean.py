# Generated by Django 3.0.2 on 2020-01-19 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toilets', '0015_auto_20200119_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='toilet',
            name='clean',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=3),
        ),
    ]
