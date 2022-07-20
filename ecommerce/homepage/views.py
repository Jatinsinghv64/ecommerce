
from pyexpat import model
from django.shortcuts import render
from django.http import HttpResponse

from backend.models import Product

from .models import *


# Create your views here.
def home(request):
	products = Product.objects.all()
	data = {
		'products' : products
	}
	return render(request, 'homepage/home.html', data)

def product_detail(request):
 return render(request, 'homepage/productdetail.html')

def login(request):
 return render(request, 'homepage/login.html')

def signup(request):
 return render(request, 'homepage/signup.html')

def order(request):
 return render(request, 'homepage/orders.html')

def profile(request):
 return render(request, 'homepage/user_profile.html')

def store(request):
	return render(request, 'homepage/store.html')


def cart(request):
	return render(request, 'homepage/cart.html')

def checkout(request):
	return render(request, 'homepage/checkout.html')




