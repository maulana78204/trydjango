from django.shortcuts import render

from .forms import ProductForm, RawProductForm
from .models import Product
#Create your views here.

def render_initial_data(request):
    initial_data = {
        'title': "My this awesome title"
    }
    obj = Product.objects.get(id=3)
    form = ProductForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "product/product_create.html", context)