# Generated by Django 2.2.5 on 2020-02-19 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house_prices', '0005_secondhandhouse_soldhouse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='renthouse',
            name='space',
            field=models.FloatField(db_column='d_space', verbose_name='面积'),
        ),
        migrations.AlterField(
            model_name='secondhandhouse',
            name='space',
            field=models.FloatField(db_column='d_space', verbose_name='面积'),
        ),
        migrations.AlterField(
            model_name='soldhouse',
            name='space',
            field=models.FloatField(db_column='d_space', verbose_name='面积'),
        ),
    ]
