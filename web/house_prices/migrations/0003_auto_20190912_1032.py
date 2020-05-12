# Generated by Django 2.2.5 on 2019-09-12 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house_prices', '0002_auto_20190912_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='taoneimianji',
            field=models.IntegerField(db_column='d_taoneimianji', verbose_name='套内面积'),
        ),
        migrations.AlterField(
            model_name='house',
            name='xiaoquweizhi',
            field=models.CharField(db_column='d_xiaoquweizhi', max_length=20, verbose_name='小区位置'),
        ),
    ]