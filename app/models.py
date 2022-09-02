from django.db import models

# Create your models here.


class Vouchers(models.Model):
    Vouchers_name = models.CharField(max_length=255)

    def __str__(self):
        return self.Vouchers_name

class Months(models.Model):
    month_name = models.CharField(max_length=255)

    def __str__(self):
        return self.month_name     



