from rest_framework import serializers


class PurchaseDrugSeriallizer(serializers.Serializer):
    drug_name = serializers.CharField(max_length=100)
    drug_type = serializers.CharField(max_length=20)
    purchase_quantity = serializers.IntegerField()


class PurchaseDrugListSerializer(serializers.Serializer):
    customer_mobile_no = serializers.CharField(max_length=15)
    customer_address = serializers.CharField(max_length=150)
    drugs = serializers.ListField(child=PurchaseDrugSeriallizer())



