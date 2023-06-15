from pstats import Stats
import statistics
from flask import views
from .models import Customer,User,Vendor
from rest_framework import generics
from .serializers import CustomerSerializer,UserLoginSerializer
from .serializers import VendorSerializer
from rest_framework.response import Response
from django.contrib.auth import login,authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status,views,serializers
from myapp import serializers
from .utils import get_user_object


# class Customer_regester(generics.ListCreateAPIView):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer

# class Vendor_registration(generics.ListCreateAPIView):
#     queryset = Vendor.objects.all()
#     serializer_class = VendorSerializer


class Customer_regester(views.APIView):
    
    def get(self, request, format=None):
        queryset = Customer.objects.all()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=statistics.HTTP_400_BAD_REQUEST)
    
class Vendor_registration(generics.ListCreateAPIView):
        queryset = Vendor.objects.all()
        serializer_class = VendorSerializer


class UserLogin(views.APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            user = authenticate(email=email, password=password)
            print("user",user)
            if user is not None:
                if user.is_active:
                    print("user login success")
                    login(request, user)
            if user is None or user.is_active == False:
                raise serializers.ValidationError(
                    'A user with this email and password is not found.'
                )
        try:
            refresh = RefreshToken.for_user(user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        user = get_user_object(user)
        if user["is_customer"]:
            profile = Customer.objects.get(customer=user["id"])
            profile = CustomerSerializer(profile).data
        elif user["is_vendor"]:
            profile = Vendor.objects.get(vendor=user["id"])
            profile = VendorSerializer(profile).data
        else:
            profile = "other profile"

        return Response({
            'user': user,
            'profile':profile,
            'token': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
