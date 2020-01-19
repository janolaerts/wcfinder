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

  ACCESSIBLE_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No')
  )

  city = models.CharField(max_length = 20, default = 'Antwerp', choices = CITIES_CHOICES)
  street = models.CharField(max_length = 50, default = None)
  number = models.IntegerField(default = None, null = True)
  reference = models.CharField(max_length = 20, blank = True)
  price = models.FloatField(default = None)
  cleaned = models.CharField(max_length = 3, default = 'Yes', choices = CLEAN_CHOICES)
  wheelchair_accessible = models.CharField(max_length = 3, default = 'Yes', choices = ACCESSIBLE_CHOICES)
  #remarks = models.TextField(default = 'No remarks')

  def __str__(self):
    return f'{self.street} {self.number}, {self.city}, ({self.reference}), {self.price}'