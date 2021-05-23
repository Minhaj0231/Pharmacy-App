from django.urls import path

from . import views

urlpatterns = [

    path('searchDrug/', views.GetDrugAvailabilityView.as_view()),

]