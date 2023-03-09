from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.core.paginator import Paginator
from .models import *

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    laptops_list = Laptops.objects.all()

    context = {
        'item_list': item_list,
        'laptops_list': laptops_list,
    }
    return render(request,'techstore/index.html', context)

def laptops(request):
    laptops_objects = Laptops.objects.all()
    search_name = request.GET.get('search_name')
    if search_name != '' and search_name is not None:
        laptops_objects = laptops_objects.filter(laptops_name__icontains=search_name)
    paginator = Paginator(laptops_objects, 4)
    page = request.GET.get('page')
    laptops_list = paginator.get_page(page)
    context = {
        'laptops_list': laptops_list,
    }
    return render(request,'techstore/laptops.html', {'laptops_list': laptops_list})

def cart_view(request):
    # Get the cart for the current user
    cart, created = Cart.objects.get_or_create(user=request.user)

    context = {}

    # Get the laptops and desktops that are in the cart
    laptops_in_cart = cart.laptops.all()
    desktops_in_cart = cart.desktops.all()

    # Add the laptops and desktops to the context if they are in the cart
    if laptops_in_cart:
        context['laptops'] = Laptops.objects.filter(pk__in=laptops_in_cart.values_list('pk', flat=True))

    if desktops_in_cart:
        context['desktops'] = Desktops.objects.filter(pk__in=desktops_in_cart.values_list('pk', flat=True))

    return render(request, 'techstore/cart.html', context)


def desktops(request):
    desktops_objects = Desktops.objects.all()
    search_name = request.GET.get('search_name')
    if (search_name != '' and search_name is not None):
        desktops_objects = desktops_objects.filter(desktops_name__icontains=search_name)

    paginator = Paginator(desktops_objects, 4)
    page = request.GET.get('page')
    desktops_list = paginator.get_page(page)
    context = {
        'desktops_list': desktops_list,
    }
    return render(request,'techstore/desktop.html', {'desktops_list': desktops_list})

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item
    }
    return render(request, 'techstore/detail.html', context)

def detaillp(request, laptops_id):
    laptops = Laptops.objects.get(pk=laptops_id)
    context = {
        'laptops': laptops
    }
    return render(request,'techstore/detail.html', context)

def detaildt(request, desktops_id):
    desktops = Desktops.objects.get(pk=desktops_id)
    context = {
        'desktops': desktops
    }
    return render(request,'techstore/detailDesktop.html', context)


def checkout(request):
    context = {}
    return render(request, 'techstore/checkout.html', context)
