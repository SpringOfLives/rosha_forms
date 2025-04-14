from django.db import models

class Audition(models.Model): 

    """
    annc stands for annoucement
    conc stands for concert
    """

    name = models.CharField(max_length=100)
    deadline = models.DateTimeField("dl", null=True, blank=True)
    annc_date = models.DateTimeField("annc", null=True, blank=True)
    conc_date = models.DateTimeField("conc", null=True, blank=True)
    poster = models.ImageField(upload_to="audition/posters/")

    def __str__(self):
        return f"{self.id} {self.name}"