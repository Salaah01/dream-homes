from django.db import models
from listings.models import Listing
from django.contrib.auth.models import User
from datetime import datetime

class Enquiry(models.Model):
    listing_id = models.ForeignKey(Listing, on_delete=models.DO_NOTHING)
    user_id = models.IntegerField(default=0, blank=True)
    user_group = models.CharField(max_length=20)
    message_date = models.DateTimeField(default=datetime.now, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(blank=True, max_length=20)
    email = models.EmailField()
    message = models.TextField(blank=True)
    searched_keywords = models.CharField(blank=True, max_length=200)
    searched_location = models.CharField(blank=True, max_length=200)
    searched_bedrooms = models.CharField(blank=True, max_length=20)
    searched_price = models.CharField(blank=True, max_length=20)
    response_to_user_id = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name