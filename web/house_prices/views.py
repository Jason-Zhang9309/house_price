from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

from house_prices.models import RentHouse,SoldHouse,SecondHandHouse
# Create your views here.

def index(request):
    return render(request, 'index.html')

def second_hand(request):
    second_hand_houses = SecondHandHouse.objects.all()
    return render(request,'second_hand.html',{'second_hand_houses':second_hand_houses})

def rent_house(request):
    rent_houses = RentHouse.objects.all()
    return render(request,'rent_house.html',{'rent_houses':rent_houses})

def sold_house(request):
    sold_houses = SoldHouse.objects.all()
    location = request.GET.get('location')
    max_total_price = request.GET.get('max_total_price')
    min_total_price = request.GET.get('min_total_price')
    if location:
        sold_houses = sold_houses.filter(location__contains=location)
    if max_total_price:
        sold_houses = sold_houses.filter(total_price__lte=max_total_price)
    if min_total_price:
        sold_houses = sold_houses.filter(total_price__gte=min_total_price)
    return render(request,'sold_house.html',{'sold_houses':sold_houses})
 

def choose(request):
    if request.method == 'GET':
    	op_guapaijia = request.GET['guapaijia']
    	op_chengjiaozhouqi = request.GET['chengjiaozhouqi']
    chosed_houses_list = houses_list
    if op_guapaijia != '':
    	chosed_houses_list = chosed_houses_list.filter(guapaijia=op_guapaijia)
    if op_chengjiaozhouqi != '':
    	chosed_houses_list = chosed_houses_list.filter(chengjiaozhouqi=op_chengjiaozhouqi)



    return render(request, 'index.html', {})