from django.db import models

class WeddingMessages(models.Model):
    fromNames = models.CharField(max_length = 200)
    message = models.CharField(max_length = 1024)
    selfie = models.ImageField(upload_to='photos/shibas_mehndi_selfies/', blank=True)


    def __str__(self):
        return f"{self.fromNames}: {self.message}"