from rest_framework import serializers
import random
from rest_framework.serializers import ModelSerializer, Serializer
from django.db import transaction
import copy
from .models import User,Customer,Vendor
import string
import random
# class UserSerializer(serializers.Serializer):
#     username = serializer.CharField(
#         max_length=50, unique=True, null=True, blank=True)
#     email = serializer.EmailField(
#         max_length=255, unique=True, null=True, blank=True)
#     phone = serializer.CharField(
#         max_length=20, unique=True, null=True, blank=True)
#     is_active = serializer.BooleanField(default=True)
#     is_admin_user = serializer.BooleanField(default=False)
#     is_vendor = serializer.BooleanField(default=False)
#     is_customer = serializer.BooleanField(default=False)
#     is_admin = serializer.BooleanField(default=False)
#     is_staff = serializer.BooleanField(default=False)
#     create_date = serializer.DateTimeField(
#         default=timezone.now, null=True, blank=True)
#     created_by = serializer.IntegerField(default=None, null=True, blank=True)
#     updated_by = serializer.IntegerField(default=None, null=True, blank=True)
#     user_type = serializer.CharField(
#         max_length=20, null=True, blank=True,default="")
 


# class CustomerSerializer(seriealizers.Serializer):
#     customer = Serializer.OneToOneField(User, on_delete=Serializer.CASCADE)
#     name = Serializer.CharField(max_length=255)
#     customer_email = Serializer.EmailField(unique=True)
#     customer_address = Serializer.CharField(max_length=255)
#     customer_phone = Serializer.CharField(max_length=20, blank=True, null=True)
#     age = Serializer.CharField(max_length=5)
#     gender = Serializer.CharField(max_length=10)
#     occupation = Serializer.CharField(max_length=50)
#     maried_status = Serializer.CharField(max_length=10)
#     class Meta:
#         db_table = "customer"



# class VendorSerializer(seriealizers.Serializer):
#     vendor = Serializer.OneToOneField(User, on_delete=Serializer.CASCADE)
#     vendor_name = Serializer.CharField(max_length=255)
#     vendor_email = Serializer.EmailField(unique=True)
#     vendor_address = Serializer.CharField(max_length=255)
#     vendor_phone = Serializer.CharField(max_length=20, blank=True, null=True)
#     org_name = Serializer.CharField(max_length=255)
#     GTS_no = Serializer.CharField(max_length=50)
# class Meta:
#         db_table = "vendor"



class CustomerSerializer(serializers.ModelSerializer):
    customer = serializers.CharField()
    name = serializers.CharField()
    customer_email = serializers.EmailField()
    customer_address = serializers.CharField()
    customer_phone = serializers.CharField()
    age = serializers.CharField()
    gender = serializers.CharField()
    occupation = serializers.CharField()
    maried_status = serializers.CharField()
    
    def to_internal_value(self, data):
        internal_data = copy.deepcopy(data)
        if internal_data.get("customer", None) == None:
            internal_data['customer'] = None
        if internal_data.get("name", None) == None:
            internal_data['name'] = None
        if internal_data.get("customer_email", None) == None:
            internal_data['customer_email'] = None
        if internal_data.get("customer_address", None) == None:
            internal_data['customer_address'] = None
        if internal_data.get("customer_phone", None) == None:
            internal_data['customer_phone'] = None
        if internal_data.get("age", None) == None:
            internal_data['age'] = None
        if internal_data.get("gender", None) == None:
            internal_data['gender'] = None
        if internal_data.get("occupation", None) == None:
            internal_data['occupation'] = None
        if internal_data.get("maried_status", None) == None:
            internal_data['maried_status'] = None
        
        return super(CustomerSerializer, self).to_internal_value(internal_data)
    def create(self, validated_data):
        request_data = copy.deepcopy(validated_data)
        with transaction.atomic():
                username = validated_data['name']+''.join([random.choice(string.digits) for i in range(0, 4)])
                password = validated_data['name'][0:4] + \
                    ''.join([random.choice(string.digits) for i in range(0, 4)])
                user = User.objects.create(username=username, email=validated_data['customer_email'],
                                        phone=validated_data['customer_phone'], is_customer=True)
                user.set_password(password)
                user.save()
                Customer.objects.create(
                    customer=user,
                    name=validated_data['name'],
                    customer_email=validated_data['customer_email'],
                    customer_address=validated_data['customer_address'],
                    customer_phone=validated_data['customer_phone'],
                    age=validated_data['age'],
                    gender=validated_data['gender'],
                    occupation=validated_data['occupation'],
                    maried_status=validated_data['maried_status'],
                    
                )
                return request_data
    class Meta:
        model = Customer
        fields = '__all__'


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email', 'password']




# vendor serializers 

class VendorSerializer(serializers.ModelSerializer):
    vendor = serializers.CharField()
    vendor_name = serializers.CharField()
    vendor_email = serializers.EmailField()
    vendor_address = serializers.CharField()
    vendor_phone = serializers.CharField()
    org_name = serializers.CharField()
    GTS_no = serializers.CharField()
    


    
    def to_internal_value(self, data):
        internal_data = copy.deepcopy(data)
        if internal_data.get("Vendor", None) == None:
            internal_data['Vendor'] = None
        if internal_data.get("vendor_name", None) == None:
            internal_data['"vendor_name'] = None
        if internal_data.get("vendor_email", None) == None:
            internal_data['vendor_email'] = None
        if internal_data.get("vendor_address", None) == None:
            internal_data['vendor_address'] = None
        if internal_data.get("vendor_phone", None) == None:
            internal_data['vendor_phone'] = None
        if internal_data.get("org_name", None) == None:
            internal_data['org_name'] = None
        if internal_data.get("GTS_no", None) == None:
            internal_data['GTS_no'] = None
       
        
        return super(VendorSerializer, self).to_internal_value(internal_data)
    def create(self, validated_data):
        request_data = copy.deepcopy(validated_data)
        with transaction.atomic():
                username = validated_data['vendor_name']+''.join([random.choice(string.digits) for i in range(0, 4)])
                # password = validated_data['vendor_name'][0:4] + \
                # ''.join([random.choice(string.digits) for i in range(0, 4)])
                password="dummy@123"

                user = User.objects.create(username=username, email=validated_data['vendor_email'],
                                        phone=validated_data['vendor_phone'], is_vendor=True)
                user.set_password(password)
                user.save()
                Vendor.objects.create(
                    vendor=user,
                    vendor_name=validated_data['vendor_name'],
                    vendor_email=validated_data['vendor_email'],
                    vendor_address=validated_data['vendor_address'],
                    vendor_phone=validated_data['vendor_phone'],
                    org_name=validated_data['org_name'],
                    GTS_no=validated_data['GTS_no'],
                    
                )
                return request_data
    class Meta:
        model = Vendor
        fields = '__all__'