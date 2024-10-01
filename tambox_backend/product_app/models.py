from django.db import models
class ProductGroup(models.Model):
    code = models.CharField(primary_key=True, max_length=6)
    description = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code


class UnitMeasurement(models.Model):
    code = models.CharField(max_length=5, unique=True)
    description = models.CharField(max_length=50)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code


class Product(models.Model):
    code = models.CharField(primary_key=True, max_length=10)
    product_group = models.ForeignKey(ProductGroup,  on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    unit_measurement = models.ForeignKey(UnitMeasurement, null=True, on_delete=models.CASCADE)
    trademark = models.CharField(max_length=40, blank=True)
    model = models.CharField(max_length=40, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=5, default=0)
    minimum_stock = models.DecimalField(max_digits=15, decimal_places=5, default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
# Create your models here.

