# Generated by Django 2.2.5 on 2020-02-17 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house_prices', '0003_auto_20190912_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentHouse',
            fields=[
                ('location', models.CharField(db_column='d_location', max_length=20, verbose_name='位置')),
                ('price', models.IntegerField(db_column='d_price', verbose_name='价格')),
                ('space', models.IntegerField(db_column='d_space', verbose_name='面积')),
                ('house_type', models.CharField(db_column='d_house_type', max_length=20, verbose_name='户型')),
                ('direction', models.CharField(db_column='d_direction', max_length=20, verbose_name='朝向')),
                ('rent_type', models.CharField(db_column='d_rent_type', max_length=20, verbose_name='租赁方式')),
                ('source_link', models.CharField(db_column='d_source_link', max_length=100, verbose_name='房源链接')),
                ('lianjia_number', models.BigIntegerField(db_column='d_lianjia_number', primary_key=True, serialize=False, verbose_name='链家编号')),
            ],
            options={
                'db_table': 'tb_rent_house',
            },
        ),
        migrations.DeleteModel(
            name='House',
        ),
    ]
