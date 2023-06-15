from django.urls import path
from .auth import Customer_regester, UserLogin
from .auth import Vendor_registration
urlpatterns = [
   path('', Customer_regester.as_view(), name='loginUser'),
   path('vendor', Vendor_registration.as_view(), name='loginVendor'),
    path('user-login/',UserLogin.as_view(),name="userlogin" ),
]

# urlpatterns = [
#    path('', Vendor_registration.as_view(), name='loginVendor'),
# ]