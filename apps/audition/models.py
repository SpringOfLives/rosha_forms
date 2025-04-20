from django.db import models

from config.utils import datetime_default

class Audition(models.Model): 

    """
    annc stands for annoucement
    conc stands for concert
    dt stands for date
    """

    name = models.CharField(max_length=100)
    deadline = models.DateTimeField(null=True, blank=True, default=datetime_default)
    annc_dt = models.DateTimeField("announcement date", null=True, blank=True, default=datetime_default)
    conc_dt = models.DateTimeField("concert", null=True, blank=True, default=datetime_default)
    poster = models.ImageField(upload_to="audition/posters/")

    def __str__(self):
        return f"{self.id} {self.name}"