from django.urls import path
from . import views
urlpatterns = [
    path('home', views.home,name='ecom-home'),
    path('product-detail', views.product_detail,name='product-detail'),
    path('', views.login,name='login-page'),
    path('signup', views.signup,name='signup-page'),
    path('order', views.order,name='order-page'),
    path('profile', views.profile,name='profile-page'),
    path('cart', views.cart, name="cart-page"),
	path('checkout', views.checkout, name="checkout-page"),
    path('store', views.store, name="store-page"),
]