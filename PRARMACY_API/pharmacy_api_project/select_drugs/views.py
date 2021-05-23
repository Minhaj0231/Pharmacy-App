from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SearchedMedicineSerializers
from rest_framework.permissions import IsAuthenticated
from .DrugAvailability import CheckDrugAvailability


# This endpoint checks if users requested drug is available or not

# endpoint request json format:
# {
#   "searchedDrugName" : "",
#   "searchedDrugType" : "",
#   "searchedDrugQuantity" : ""
# }

# endpoint  response format:
#
# {
#     "availability" : "",
#     "quantity": ""
#     "per_unit_price": ""
# }


class GetDrugAvailabilityView(APIView):
    permission_classes = (IsAuthenticated,)  # only logged in user will be able to use this endpoint

    def post(self, request):

        serializer = SearchedMedicineSerializers(data=request.data)

        # user requests with correct json format
        if serializer.is_valid():
            serialized_data = serializer.data

            drug_availability_object = CheckDrugAvailability()

            check_availability = drug_availability_object.check_availability(serialized_data)

            return Response({"availability": "{}".format(check_availability.get("availability")),
                             "quantity": "{}".format(check_availability.get("quantity")),
                             "per_unit_price": "{}".format(
                                 check_availability.get("per_unit price"))})  # available quantity of searched drug

        # user requests with wrong json format
        else:
            return Response({"errors": serializer.errors})
