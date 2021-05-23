from django.shortcuts import render, redirect
import requests


def search_drug_view(request):
    print(request.session["selected_drugs"])
    return render(request, 'search_drugs/search_drugs.html')


def search_detail_view(request):
    drugs = {"searchedDrugName": request.POST["drug_name"],
             "searchedDrugType": request.POST["drug_type"],
             "searchedDrugQuantity": request.POST["drug_quantity"]
             }

    url = 'http://127.0.0.1:8000/select_drugs/searchDrug/'
    header = {

        'Authorization': "Token {}".format(request.session['token'])
    }

    response = requests.post(url, drugs, headers=header)

    data = response.json()

    drug_detail = {
        'avaibility': data["availability"],
        'drug': request.POST["drug_name"],
        'type': request.POST["drug_type"],
        'price': data["per_unit_price"],
        'quantity': data["quantity"]
    }

    request.session["drug_detail"] = drug_detail

    return render(request, 'search_drugs/search_result.html', {'data': data})


def save_drug(request):
    drug_info = request.session["drug_detail"]
    drug_info["idx"] = len(request.session["selected_drugs"])
    if drug_info["avaibility"] == "not_available":
        return redirect("search_drug")


    else:

        drug_list = request.session["selected_drugs"]
        drug_list.append(drug_info)
        request.session["selected_drugs"] = drug_list

    return redirect("show_drugs")


def show_drugs(request):
    drug_list = request.session["selected_drugs"]

    return render(request, 'search_drugs/show_drugs.html', {"drug_list": drug_list})


def remove_drugs(request, idx):
    drug_list = request.session["selected_drugs"]
    drug_list.pop(idx)


    i = 0;
    for drug in drug_list:
        drug["idx"] = i
        i = i + 1

    request.session["selected_drugs"] = drug_list

    return redirect("show_drugs")




def user_info(request):
    if request.method == "POST":
        user_info = { "mobile" : request.POST["mobile_number"],
                        "address" : request.POST["address"]
        }

        request.session["user_info"] = user_info

        return  redirect("purchase")

    return  render(request,"search_drugs/user_info.html" )

def purchase(request):
    user_info = request.session["user_info"]


    drugs = []
    drug_list = request.session["selected_drugs"]

    for drug in drug_list :


        drugs.append( {
            "drug_name": "{}".format(drug['drug']) ,
            "drug_type": "{}".format(drug['type']),
            "purchase_quantity": "{}".format(drug["quantity"])
        })



    data = {"customer_mobile_no": user_info["mobile"],
            "customer_address": user_info["address"],

            "drugs": drugs

            }

    url = 'http://127.0.0.1:8000/purchase_drugs/purchase/'
    header = {

        'Authorization': "Token {}".format(request.session['token'])
    }

    response = requests.post(url, data, headers=header)


    data = response.json()
    print(data)

    text = 'purchase successful'

    return render(request, 'search_drugs/purchase.html', {"data" : text})





