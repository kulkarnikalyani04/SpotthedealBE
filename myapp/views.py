from rest_framework.generics import ListCreateAPIView
from .models import Customer,User,Vendor,Product
from .serializer import ProductSerializer
from rest_framework.response import Response
from rest_framework import status,views,serializers
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http import Http404
from rest_framework.filters import OrderingFilter
from .utils import AssessmentPageNumberPagination

class ProductAPI(views.APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(views.APIView):
    """
    Retrieve, update or delete a product instance.
    """
    permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except ProductSerializer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Product = self.get_object(pk)
        serializer = ProductSerializer(Product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Product = self.get_object(pk)
        serializer = ProductSerializer(Product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ProductFilter(ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [OrderingFilter]
    filterset_fields = ['product_price']
    pagination_class = AssessmentPageNumberPagination
