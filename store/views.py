from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'store/index.html')


def nosotros(request):
    return render(request, 'store/nosotros.html')


def DetailProduct(request, product_id):
    return render(request, 'store/detailproduct.html', {'id': product_id})


def CategoryForm(request):
    return render(request, 'store/formcategoria.html')


def ProductForm(request):
    return render(request, 'store/formproducto.html')


def PagoForm(request):
    return render(request, 'store/formpago.html')


def ContactForm(request):
    return render(request, 'store/contactos.html')
