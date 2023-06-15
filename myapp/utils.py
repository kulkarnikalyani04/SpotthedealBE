from django.forms.models import model_to_dict
from rest_framework.pagination import PageNumberPagination

def get_user_object(user):
    user = model_to_dict(user)
    del user['password']
    userType = ''
    if user['is_customer']:
        userType = "CUSTOMER"
    if user['is_vendor']:
        userType = "VENDOR"
    if user['is_admin_user'] or user['is_superuser']:
        userType = "SUPERADMIN"
    user['user_type'] = userType
    return user


class AssessmentPageNumberPagination(PageNumberPagination):
    page_size = 2
    page_query_param = "p"
    page_size_query_param = "records"
    