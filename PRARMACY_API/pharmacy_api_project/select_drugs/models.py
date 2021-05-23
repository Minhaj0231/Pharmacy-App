from django.db import models


class Drugs(models.Model):
    drug_name = models.CharField(max_length=100, unique=True,default="no_name")
    drug_type = models.CharField(max_length=20, default="no_type")  # tablet/syrup/ nebulizer/ Eye drops/... etc
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.IntegerField()

    def __str__(self):
        return self.drug_name


