from django.urls import path

from  .views import search_drug_view, search_detail_view,save_drug, show_drugs, remove_drugs, purchase, user_info
urlpatterns = [

    path('', search_drug_view, name='search_drug'),
    path('searchresult/',search_detail_view, name="search_details" ),
    path("save/", save_drug, name = "save"),
    path("drug_list/", show_drugs, name = "show_drugs"),
    path("remove_drugs/<int:idx>/", remove_drugs, name = "remove_drugs"),
    path("purchase/", purchase, name = 'purchase'),
    path("user_info/", user_info, name  = 'user_info'),



]