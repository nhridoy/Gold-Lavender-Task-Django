from random import randint

from django.db import models


def random_with_N_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Phone(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='phone_brand')
    model_name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='phone/', blank=True, default='phone/default.png')
    colors = models.CharField(max_length=255)
    jan_code = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        janCode = random_with_N_digits(15)
        self.jan_code = janCode
        super(Phone, self).save(*args, **kwargs)
