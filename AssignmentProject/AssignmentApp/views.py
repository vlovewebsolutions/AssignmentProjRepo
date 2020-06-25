
#from django.shortcuts import render
#from django.http import HttpResponse
#from rest_framework import viewsets
#from .models import Product
#from .serializers import ProductSerializer
#from .forms import ProductForm


#class ProductViewSet(viewsets.ModelViewSet):
#    queryset = Product.objects.all().order_by('ProductName')
#    serializer_class = ProductSerializer


from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        
        Product_Name = request.query_params.get('ProductName', None)
        if Product_Name is not None:
            products = productss.filter(Product_Name__icontains=title)
        
        products_serializer = ProductSerializer(products, many=True)
        return JsonResponse(products_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        product_data = JSONParser().parse(request)
        products_serializer = ProductSerializer(data=product_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse(products_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(products_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Product.objects.all().delete()
        return JsonResponse({'message': '{} Productrs were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    try: 
        product = Product.objects.get(pk=pk) 
    except Product.DoesNotExist: 
        return JsonResponse({'message': 'The Products does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        product_serializer = ProductSerializer(product) 
        return JsonResponse(product_serializer.data) 
 
    elif request.method == 'PUT': 
        product_data = JSONParser().parse(request) 
        product_serializer = ProductSerializer(product, data=product_data) 
        if product_serializer.is_valid(): 
            product_serializer.save() 
            return JsonResponse(product_serializer.data) 
        return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        product.delete() 
        return JsonResponse({'message': 'Product was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def product_list_published(request):
    product = Product.objects.filter(published=True)
        
    if request.method == 'GET':
        products_serializer = ProductSerializer(product, many=True)
        return JsonResponse(products_serializer.data, safe=False)
