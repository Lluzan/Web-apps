from django.shortcuts import render
from .models import Articles
from django.views.generic import DetailView


def products_home(request):
    usluga = Articles.objects.order_by('-date')
    return render(request, 'products/product_home.html', {'usluga': usluga})



