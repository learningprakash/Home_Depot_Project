from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Customers(models.Model):
    CompanyName = models.CharField(max_length=100)
    CustomerSpend = models.DecimalField(max_digits=10, decimal_places=2)
    # @property
    # def CustomerSpend(self):
    #     return "$%s" % self.CustomerSpend
    IsPro = models.BooleanField()
    Password = models.CharField(max_length=100)
    Rating = models.DecimalField(max_digits=10, decimal_places=2)
    Zip = models.CharField(max_length=6)
    IsAvailable = models.BooleanField()


class CategoryCustomerMap(models.Model):
    Category = models.CharField(max_length=100)
    CustomerId = models.CharField(max_length=100)


class KeywordCategoryUrlMap(models.Model):
    Keyword = models.CharField(max_length=300)
    Category = models.CharField(max_length=100)
    Url = models.CharField(max_length=200, null=True)

