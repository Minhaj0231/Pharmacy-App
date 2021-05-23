from .models import Drugs


# checks if drug is available or not
class CheckDrugAvailability:

    def __init__(self):
        pass






    # checks the availability for searched drug
    # parameter: SearchedMedicineSerializers object's  valid data
    # return type dictionary{"availability" :"",
    #                         "quantity":  }
    def check_availability(self, drug_info):

        availability = {}

        query_row_count = Drugs.objects.filter(drug_name=drug_info.get("searchedDrugName"),
                                               drug_type=drug_info.get("searchedDrugType")).count()
        # searched drugs not found
        if query_row_count == 0:

            availability["availability"] = "not_available"
            availability["quantity"] = 0
            availability["per_unit price"] = 0
        # searched drug found
        else:
            drug = Drugs.objects.get(drug_name=drug_info.get("searchedDrugName"),
                                     drug_type=drug_info.get("searchedDrugType"))

            # drug is found but don't have any available quantity
            if drug.quantity_available <= 0:

                availability["availability"] = "not_available"
                availability["quantity"] = 0
                availability["per_unit price"] = drug.price_per_unit

            # available drug quantity is less then searched quantity
            elif drug.quantity_available < drug_info.get("searchedDrugQuantity"):

                availability["availability"] = "partially_available"
                availability["quantity"] = drug.quantity_available
                availability["per_unit price"] = drug.price_per_unit

            # searched drug is available
            else:
                availability["availability"] = "available"
                availability["quantity"] = drug_info.get("searchedDrugQuantity")
                availability["per_unit price"] = drug.price_per_unit

        return availability




        


