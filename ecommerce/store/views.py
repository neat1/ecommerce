from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.http import JsonResponse

# Create your views here.

def store(request):
	context = {}
	return render(request, 'store/store.html', context)

def cart(request):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		items = []
		order = {'get_cart_total': 0, 'get_cart_items':0}

	context = {'items':items, 'order':order,}
	return render(request, 'store/cart.html', context)

def checkout(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		items = []
		order = {'get_cart_total': 0, 'get_cart_items':0}

	context = {'items':items, 'order':order,}
	return render(request, 'store/checkout.html', context)

def men(request):
	context = {}
	return render(request, 'store/men.html', context)

def women(request):
	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'store/women.html', context)

def home(request):
	context = {}
	return render(request, 'store/home.html', context)

def main(request):
	context = {}
	return render(request, 'store/main.html', context)

def checkout_summary(request):
	context = {}
	return render(request, 'store/your_cart.html', context)

def navbar(request):
	context = {}
	return render(request, 'store/navbar.html', context)
