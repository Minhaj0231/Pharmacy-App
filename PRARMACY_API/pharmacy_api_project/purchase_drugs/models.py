from django.db import models


class SaleRecord(models.Model):

    customer_id = models.ForeignKey("auth.User", on_delete= models.CASCADE)
    date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    customer_mobile_no = models.CharField(max_length=15)
    customer_address = models.CharField(max_length=150)

    def __str__(self):
        return str(self.id)


class SoldDrugs(models.Model):

    sale_id = models.ForeignKey("SaleRecord", on_delete= models.CASCADE)
    drug_id = models.ForeignKey("select_drugs.Drugs", on_delete= models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.id)
