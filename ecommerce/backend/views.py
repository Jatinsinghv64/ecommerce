# from django.shortcuts import render
from urllib import response
from rest_framework.response import Response
from rest_framework.generics import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework import permissions
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import *


class RegisterView(GenericAPIView):

    serializer_class = CustomerSerializer

    def post(self,request):

        serializer = self.serializer_class(data=request.data)  
        serializer.is_valid(raise_exception=True)
        
        return Response({"status":"success"})


class LoginView(TokenObtainPairView):
	"""
	Login View with jWt token authentication
	"""
	serializer_class = MyTokenObtainPairSerializer

# class testView(GenericAPIView):
#     permission_classes = (permissions.IsAuthenticated,)
#     serializer_class = CustomerSerializer

#     def get(self,request):

#         return Response({"status":"working"})

@api_view(['GET'])
def getData(request):
    products = Product.objects.all()
    serializer = ProductSerializers(products, many=True)
    return Response(serializer.data)