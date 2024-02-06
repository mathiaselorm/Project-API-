from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ProductSerializer
from .serializers import UserRegistrationSerializer
from .models import Product
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView


@api_view(['GET'])
def apioverview(request):
    api_urls = {
        'List': '/user_list/',
        'Detail View': '/user_detail/<str:pk>/',
        'Create': '/user_create/',
        'Update': '/user_update/<str:pk>/',
        'Delete': '/user_delete/<str:pk>/',
    }
    
    return Response(api_urls)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def product_list(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def product_create(request):
    
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def product_detail(request, pk):
    try:
        product_instance = Product.objects.get(id=pk)
        serializer = ProductSerializer(product_instance, many=False)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response({"detail": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def product_update(request, pk):
    product_instance = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product_instance, data=request.data, partial = True, many=False)
    if serializer.is_valid():
        serializer.save()
        
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def product_delete(request, pk):
    product_instance = get_object_or_404(Product, id=pk)
    product_instance.delete()
    
    return Response('Item successfully deleted')



@api_view(['POST'])
def user_signup(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)