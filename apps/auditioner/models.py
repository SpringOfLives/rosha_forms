from django.db import models
from django.core.validators import RegexValidator
from apps.audition.models import Audition

class Auditioner(models.Model):

    audition = models.ForeignKey(Audition, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    nationality = models.CharField(max_length=255)
    phone = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^[0-9]'
            )
        ]
    )
    email = models.EmailField()
    instrument = models.CharField(max_length=100)
    
    def __str__(self):
        return f"No.{self.id} {self.name}"
