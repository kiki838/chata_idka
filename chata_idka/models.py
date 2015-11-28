from django.db import models

class Temperature(models.Model):
    temp = models.DecimalField(max_digits=5, decimal_places=1)
    date = models.DateTimeField()



