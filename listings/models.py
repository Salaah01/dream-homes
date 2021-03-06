from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Listing(models.Model):
    agent = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        limit_choices_to={'groups__name': 'Agent'}
    )
    title = models.CharField(max_length=200)
    address = models.CharField(max_length = 200)
    city = models.CharField(max_length = 30)
    postcode = models.CharField(max_length = 10)
    longitude = models.FloatField()
    latitude = models.FloatField()
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField(default=1)
    garage = models.IntegerField(default=0)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
