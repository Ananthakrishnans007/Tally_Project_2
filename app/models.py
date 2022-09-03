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


class Voucher_Register(models.Model):
    Voucher = models.ForeignKey(Vouchers,on_delete=models.CASCADE)
    Month =models.ForeignKey(Months,on_delete=models.CASCADE)
    Date = models.DateField()
    Particulars = models.CharField(max_length=255)
    # Vch_Type = models.CharField(max_length=255)
    # Vch_No = models.IntegerField()
    Debit_Amount = models.IntegerField(default="",null=True,blank=True)
    Credit_Amount = models.IntegerField(default="",null=True,blank=True)

    def __str__(self):
        return self.Voucher.Vouchers_name

class Voucher_count(models.Model):
    Voucher = models.ForeignKey(Vouchers,on_delete=models.CASCADE)
    Month =models.ForeignKey(Months,on_delete=models.CASCADE)
    Total_Voucher = models.IntegerField(default="",null=True,blank=True)
    # Cancelled = models.IntegerField(default="",null=True,blank=True)

    def __str__(self):
        return self.Voucher.Vouchers_name


class Total(models.Model):
    Voucher = models.ForeignKey(Vouchers,on_delete=models.CASCADE)
    Total = models.IntegerField(default="",null=True,blank=True)

    def __str__(self):
        return self.Voucher.Vouchers_name



