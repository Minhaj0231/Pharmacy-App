from django.urls import include, path

from .views import FacebookLogin

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),   # for login and logout
    path('rest-auth/registration/', include('rest_auth.registration.urls')),  # for registration
    path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login')  #for facebook log in
]