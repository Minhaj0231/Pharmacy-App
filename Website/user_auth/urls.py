from django.urls import path

from .views import home, log_in,  sign_up, log_out

urlpatterns = [

    path('', home, name='home'),
    path('log_in/', log_in, name='log_in'),
    path('registration/', sign_up, name='sign_up'),
    path('logout/',log_out, name = "log_out" )
]
