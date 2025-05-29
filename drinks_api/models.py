from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    image_url = models.URLField(blank=True)
    description = models.TextField()
    def __str__(self):
        return self.name


