from django.contrib import admin

# Register your models here.

from house_prices.models import RentHouse,SoldHouse,SecondHandHouse

class RentHouseAdmin(admin.ModelAdmin):

    list_display = ('location','price','space','house_type','direction','rent_type','source_link','lianjia_number',)
    ordering = ('lianjia_number', )

class SoldHouseAdmin(admin.ModelAdmin):

    list_display = ('location','total_price','space','single_price','house_type','direction','open_date','sold_date','source_link','lianjia_number',)
    ordering = ('lianjia_number', )

class SecondHandHouseAdmin(admin.ModelAdmin):

    list_display = ('location','total_price','space','single_price','house_type','direction','open_date','source_link','lianjia_number',)
    ordering = ('lianjia_number', )

admin.site.register(RentHouse, RentHouseAdmin)
admin.site.register(SoldHouse, SoldHouseAdmin)
admin.site.register(SecondHandHouse, SecondHandHouseAdmin)