from django.db import models
from .utils import INSTRUMENT_TYPE
from config.utils import datetime_default


class Audition(models.Model):
    """
    annc stands for annoucement
    conc stands for concert
    dt stands for date
    """

    name = models.CharField(max_length=100, unique=True)
    deadline = models.DateTimeField(null=True, blank=True, default=datetime_default)
    annc_dt = models.DateTimeField(
        "announcement date", null=True, blank=True, default=datetime_default
    )
    conc_dt = models.DateTimeField(
        "concert", null=True, blank=True, default=datetime_default
    )
    poster = models.ImageField(upload_to="audition/posters/")
    instrument = models.ManyToManyField("Instrument")

    def __str__(self):
        return f"{self.id} {self.name}"

class Instrument(models.Model):

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=INSTRUMENT_TYPE, default="SOLO", verbose_name="instrument_type")

    def __str__(self):
        return f"{self.name} {self.type}"