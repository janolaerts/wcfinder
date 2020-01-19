# Generated by Django 3.0.2 on 2020-01-19 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toilets', '0011_auto_20200119_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='toilet',
            name='clean',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=3),
        ),
        migrations.AlterField(
            model_name='toilet',
            name='city',
            field=models.CharField(choices=[('Antwerp', 'Antwerp'), ('Bruges', 'Bruges'), ('Brussels', 'Brussels'), ('Charleroi', 'Charleroi'), ('Ghent', 'Ghent'), ('Hasselt', 'Hasselt'), ('Kortrijk', 'Kortrijk'), ('Leuven', 'Leuven'), ('Liege', 'Liege'), ('Mechelen', 'Mechelen'), ('Mons', 'Mons'), ('Namur', 'Namur'), ('Nivelles', 'Nivelles'), ('Ostend', 'Ostend'), ('Tournai', 'Tournai')], default='Antwerp', max_length=20),
        ),
    ]
