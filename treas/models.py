from django.db import models

# Create your models here.
class Treasurelist(models.Model):
    name = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=10,decimal_places=2)
    location = models.CharField(max_length=50)
    img_url = models.CharField(max_length=100)

    def __str__(self):
        return self.name