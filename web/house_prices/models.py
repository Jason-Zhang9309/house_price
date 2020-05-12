from django.db import models

# Create your models here.
class RentHouse(models.Model):
    
    location = models.CharField(max_length=20, db_column='d_location', verbose_name='位置')
    price = models.IntegerField(db_column='d_price', verbose_name='价格')
    space = models.FloatField(db_column='d_space', verbose_name='面积')
    house_type = models.CharField(max_length=20, db_column='d_house_type', verbose_name='户型')
    direction  = models.CharField(max_length=20, db_column='d_direction', verbose_name='朝向')
    rent_type =  models.CharField(max_length=20, db_column='d_rent_type', verbose_name='租赁方式')
    source_link = models.CharField(max_length=100, db_column='d_source_link', verbose_name='房源链接')
    lianjia_number = models.BigIntegerField(primary_key=True, db_column='d_lianjia_number', verbose_name='链家编号')

    class Meta:
        db_table = 'tb_rent_house'


class SecondHandHouse(models.Model):
    
    location = models.CharField(max_length=20, db_column='d_location', verbose_name='位置')
    total_price = models.IntegerField(db_column='d_total_price', verbose_name='总价')
    space = models.FloatField(db_column='d_space', verbose_name='面积')
    single_price = models.IntegerField(db_column='d_single_price', verbose_name='单价')
    house_type = models.CharField(max_length=20, db_column='d_house_type', verbose_name='户型')
    direction  = models.CharField(max_length=20, db_column='d_direction', verbose_name='朝向')
    open_date = models.DateField(db_column='d_open_date', verbose_name='挂牌日期')
    source_link = models.CharField(max_length=100, db_column='d_source_link', verbose_name='房源链接')
    lianjia_number = models.BigIntegerField(primary_key=True, db_column='d_lianjia_number', verbose_name='链家编号')

    class Meta:
        db_table = 'tb_second_hand_house'


class SoldHouse(models.Model):
    
    location = models.CharField(max_length=20, db_column='d_location', verbose_name='位置')
    total_price = models.IntegerField(db_column='d_total_price', verbose_name='总价')
    space = models.FloatField(db_column='d_space', verbose_name='面积')
    single_price = models.IntegerField(db_column='d_single_price', verbose_name='单价')
    house_type = models.CharField(max_length=20, db_column='d_house_type', verbose_name='户型')
    direction  = models.CharField(max_length=20, db_column='d_direction', verbose_name='朝向')
    open_date = models.DateField(db_column='d_open_date', verbose_name='挂牌日期')
    sold_date = models.DateField(db_column='d_sold_date', verbose_name='成交日期')
    source_link = models.CharField(max_length=100, db_column='d_source_link', verbose_name='房源链接')
    lianjia_number = models.BigIntegerField(primary_key=True, db_column='d_lianjia_number', verbose_name='链家编号')

    class Meta:
        db_table = 'tb_sold_house'
