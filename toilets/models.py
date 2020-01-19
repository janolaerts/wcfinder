from django.db import models

# Create your models here.
class Toilet(models.Model):
  CITIES_CHOICES = (
    ('Antwerp', 'Antwerp'),
    ('Bruges', 'Bruges'),
    ('Brussels', 'Brussels'),
    ('Charleroi', 'Charleroi'),
    ('Ghent', 'Ghent'),
    ('Hasselt', 'Hasselt'),
    ('Kortrijk', 'Kortrijk'),
    ('Leuven', 'Leuven'),
    ('Liege', 'Liege'),
    ('Mechelen', 'Mechelen'),
    ('Mons', 'Mons'),
    ('Namur', 'Namur'),
    ('Nivelles', 'Nivelles'),
    ('Ostend', 'Ostend'),
    ('Tournai', 'Tournai'),
  )

  CLEAN_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No')
  )

  city = models.CharField(max_length = 20, default = 'Antwerp', choices = CITIES_CHOICES)
  street = models.CharField(max_length = 50, default = None)
  number = models.IntegerField(default = None)
  reference = models.CharField(max_length = 20)
  price = models.FloatField(default = None)
  remarks = models.TextField(default = 'No remarks')

  def __str__(self):
    return f'{self.street} {self.number}, {self.city}, ({self.reference}), {self.price}, {self.remarks}'