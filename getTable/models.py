from django.db import models

# Create your models here.
class Ad(models.Model):
    AdId = models.CharField(max_length=20)
    totalViews = models.IntegerField()
    todayViews = models.IntegerField()
    promoStatus = models.CharField(max_length=6)