from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.contrib.auth.models import UserManager
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=50, unique=True, null=True, blank=True)
    email = models.EmailField(
        max_length=255, unique=True, null=True, blank=True)
    phone = models.CharField(
        max_length=20, unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin_user = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    create_date = models.DateTimeField(
        default=timezone.now, null=True, blank=True)
    created_by = models.IntegerField(default=None, null=True, blank=True)
    updated_by = models.IntegerField(default=None, null=True, blank=True)
    user_type = models.CharField(
        max_length=20, null=True, blank=True,default="")
    USERNAME_FIELD = 'email'
    objects = UserManager()
    class Meta:
        db_table = "User"
        verbose_name = 'User'
        verbose_name_plural = 'Users'

# class Customer_reg(models.Model):
#     f_name = models.CharField(max_length=255)
#     l_name = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     address = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
#     c_password = models.CharField(max_length=255)

class Customer(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    customer_email = models.EmailField(unique=True)
    customer_address = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=20, blank=True, null=True)
    age = models.CharField(max_length=5)
    gender = models.CharField(max_length=10)
    occupation = models.CharField(max_length=50)
    maried_status = models.CharField(max_length=10)
    class Meta:
        db_table = "customer"


class Vendor(models.Model):
    vendor = models.OneToOneField(User, on_delete=models.CASCADE)
    vendor_name = models.CharField(max_length=255)
    vendor_email = models.EmailField(unique=True)
    vendor_address = models.CharField(max_length=255)
    vendor_phone = models.CharField(max_length=20, blank=True, null=True)
    org_name = models.CharField(max_length=255)
    GTS_no = models.CharField(max_length=50)
    class Meta:
        db_table = "vendor"
