from django.db import models

class FarmerDetails(models.Model):
    username = models.EmailField(max_length=100)
    email = models.CharField(max_length=25)  
    password = models.CharField(max_length=30)  # in quintals

    def __str__(self):
        return self.username
