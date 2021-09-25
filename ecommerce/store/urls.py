from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.home, name="home"),
	path('main/', views.main, name="main"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('men/', views.men, name="men"),
	path('women/', views.women, name="women"),
	path('durability/', views.durability, name="durability"),

 
]
