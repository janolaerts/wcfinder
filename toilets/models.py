from django.db import models

# Create your models here.
class Toilet(models.Model):
  city = models.CharField(max_length = 20, default = None)
  street = models.CharField(max_length = 50, default = None)
  number = models.IntegerField(default = None)
  reference = models.CharField(max_length = 20)
  price = models.FloatField(default = None)
  remarks = models.TextField(default = 'No remarks')

  def __str__(self):
    return f'{self.street} {self.number}, {self.city}, ({self.reference})'