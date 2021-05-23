from rest_framework import serializers


class SearchedMedicineSerializers(serializers.Serializer):

    searchedDrugName = serializers.CharField(required=True, max_length=100)
    searchedDrugType = serializers.CharField(required=True, max_length=100)
    searchedDrugQuantity = serializers.IntegerField(required=True)
