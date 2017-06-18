from django.contrib.auth.models import User
from django.db import models


class CarPhoto(models.Model):
    #photo
    photo = models.ImageField(width_field="width_field", height_field="height_field")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)

    #details
    pub_date = models.DateField('date published')
    author = models.ForeignKey(User)
    brand = models.CharField(max_length=250)
    model = models.CharField(max_length=250)
