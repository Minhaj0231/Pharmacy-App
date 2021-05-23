import datetime
from select_drugs.models import Drugs
from .models import SaleRecord, SoldDrugs


# get drugs per_unit price from Drugs model
class DrugPricePerUnit:

    def __init__(self):
        pass

    # get drugs per_unit price from Drugs model
    # parameter = purchased drug name and purchased drug type
    # return type = drug's per unit price
    def get_price_per_unit(self, drug_name, drug_type):
        drug = Drugs.objects.get(drug_name=drug_name,
                                 drug_type=drug_type)

        return drug.price_per_unit


# calculates total amount of purchased drugs
class CalculateTotalAmount:

    def __init__(self):
        pass

    # calculates total amount of purchases drugs
    # parameter = purchased drugs list
    # return type = total price of perchased drugs
    def get_total_amnt(self, drug_list):

        total_price = 0

        drug_price_per_unit_object = DrugPricePerUnit()
        for drugs in drug_list:
            total_price_per_drug = drug_price_per_unit_object.get_price_per_unit(drugs["drug_name"],
                                                                                drugs["drug_type"]) * drugs["purchase_quantity"]

            total_price += total_price_per_drug

            return total_price


# saves record to SaleRecord Table
class SaveToSaleRecord:

    def __init__(self):
        pass

    # saves record to SaleRecord Table
    # parameter = purchased_customer_object, total_price,  purchased_custoemr_mobile_no,  purchased_custoemr_address
    # return type =  created SaleRecord object
    def save(self, purchased_customer_id, total_price,  purchased_custoemr_mobile_no,  purchased_custoemr_address):
        sale_record_object = SaleRecord(customer_id = purchased_customer_id, date =datetime.datetime.now() , total_price = total_price,
                                        customer_mobile_no = purchased_custoemr_mobile_no, customer_address = purchased_custoemr_address)

        sale_record_object.save()
        return sale_record_object


# updates Drugs table after  purchase
class UpdateDrugTable:
    def __init__(self):
        pass

    # uupdate quantity_available attribute of Drugs table after purchase
    # parameter = purchased drugs list
    # return type = doesnt return anything
    def update_table(self,drug_list):

        for drugs in drug_list:
            drug_object = Drugs.objects.get(drug_name=drugs["drug_name"],
                                            drug_type=drugs["drug_type"])
            drug_object.quantity_available = drug_object.quantity_available - drugs["purchase_quantity"]

            drug_object.save()


# saves record to SoldDrugs  Table
class SaveToSoldDrugs:   # shouldn't create this class object before calling save method of SaleRecord object
    def __init__(self):
        pass
    # saves record of sold drugs to SoldDrugs Table after purchase
    # parameter = SaleRecord object, purchased drug_list
    # return type = doesn't return anything
    def save(self,sale_record_object, drug_list):  # shouldn't call this method before  calling save method of SaleRecord object

        for drugs in drug_list:
            drug_object = Drugs.objects.get(drug_name=drugs["drug_name"],
                                            drug_type=drugs["drug_type"])

            total_price_per_drug = drug_object.price_per_unit * drugs["purchase_quantity"]

            sold_drugs_object = SoldDrugs(sale_id = sale_record_object, drug_id = drug_object,
                                          quantity = drugs["purchase_quantity"], price = total_price_per_drug)

            sold_drugs_object.save()

















