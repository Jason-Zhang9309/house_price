from django.urls import path
from house_prices import views

urlpatterns = [
        path('', views.index, name='index'),
        path('second_hand', views.second_hand, name='second_hand'),
        path('rent_house', views.rent_house, name='rent_house'),
        path('sold_house', views.sold_house, name='sold_house'),
        path('choose', views.choose, name='choose'),
        ]
