from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:product_id>/', views.DetailProduct, name='detail_product'),
    path('category/', views.CategoryForm, name='form_category'),
    path('product/', views.ProductForm, name='form_product'),
    path('payment/', views.PagoForm, name='form_payment'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('contact/', views.ContactForm, name='contact_form'),
]
