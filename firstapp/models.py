from django.db import models

# Create your models here.

class Food(models.Model):
    foodId = models.IntegerField(default=1, primary_key=True, serialize=False, verbose_name='ID')),
    name = models.CharField(default="Name",max_length = 200)
    brand = models.CharField(default="Brand",max_length = 200)
    