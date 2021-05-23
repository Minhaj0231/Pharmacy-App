from django.urls import path

from . import views

urlpatterns = [

    path('purchase/', views.PurchaseView.as_view()),

]