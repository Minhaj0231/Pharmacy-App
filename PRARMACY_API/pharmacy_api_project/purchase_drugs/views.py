
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import PurchaseDrugListSerializer
from .purchase import CalculateTotalAmount, SaveToSaleRecord, SaveToSoldDrugs, UpdateDrugTable


class PurchaseView(APIView):
    permission_classes = (IsAuthenticated,)  # only logged in user will be able to use this endpoint

    def post(self,request):
        serializer = PurchaseDrugListSerializer(data=request.data)

        # user requests with correct json format
        if serializer.is_valid():

            serialized_data = serializer.data

            calculate_total_amount_object = CalculateTotalAmount()
            total_price = calculate_total_amount_object.get_total_amnt(serialized_data["drugs"])

            save_to_sale_record_object = SaveToSaleRecord()
            sale_record_object = save_to_sale_record_object.save(request.user,total_price,
                                                             serialized_data["customer_mobile_no"],serialized_data["customer_address"])

            update_drug_table_object = UpdateDrugTable()
            update_drug_table_object.update_table(serialized_data["drugs"])

            save_to_sold_drugs_object = SaveToSoldDrugs()
            save_to_sold_drugs_object.save(sale_record_object,serialized_data["drugs"])

            return Response({"totalPrice": "{}".format(total_price)})

            # user requests with wrong json format
        else:

            return Response({"errors": serializer.errors})








