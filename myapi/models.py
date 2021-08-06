from django.db import models


class Bmi(models.Model):
    weight = models.FloatField()
    height = models.FloatField()
    bmi = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user
