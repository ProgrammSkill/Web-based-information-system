from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Models (models.Model):
    мodel = models.CharField (max_length = 50, verbose_name = 'Модель марки')

class Brands (models.Model):
    brand = models.CharField (max_length = 50, verbose_name = 'Марка автозапчасти')

class BrandsAndModels (models.Model):
    id_brand = models.ForeignKey('Brands', on_delete = models.PROTECT, verbose_name = 'Марка автомобиля')
    id_model = models.ForeignKey('Models', on_delete = models.PROTECT, verbose_name = 'Модель')

class Cities (models.Model):
    city = models.CharField (max_length = 50, verbose_name = 'Город')

class Streets (models.Model):
    street = models.CharField (max_length = 50, verbose_name = 'Улица')

class Manufacturers (models.Model):
    manufacturer = models.CharField (max_length = 50, verbose_name = 'Производитель')

class StoreDepartments (models.Model):
    id_city = models.ForeignKey('Cities', on_delete=models.PROTECT, verbose_name='Город')
    id_street = models.ForeignKey('Streets', on_delete=models.PROTECT, verbose_name='Улица')
    house = models.CharField (max_length = 10, verbose_name = 'Дом')
    telephone = models.CharField (max_length = 20, verbose_name = 'Телефон')

class AutoParts (models.Model):
    vendor_code = models.CharField (max_length=20, verbose_name='Артикул')
    name = models.CharField(max_length=20, verbose_name='Наименование')
    id_brand_and_models = models.ForeignKey('BrandsAndModels', on_delete=models.PROTECT, verbose_name='Автомобиль')
    id_manufacturer = models.ForeignKey('Manufacturers', on_delete=models.PROTECT, verbose_name='Производитель')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    comment = models.TextField(verbose_name='Комментарий')

class AutoPartsInStock (models.Model):
    id_StoreDepartment = models.ForeignKey('StoreDepartments', on_delete=models.PROTECT, verbose_name='Магазин')
    id_StoreDepartment = models.ForeignKey('AutoParts', on_delete=models.PROTECT, verbose_name='Автозапчасть')
    name = models.CharField(max_length=20, verbose_name='Наименование')
    id_brand_and_models = models.ForeignKey('BrandsAndModels', on_delete=models.PROTECT, verbose_name='Автомобиль')
    id_manufacturer = models.ForeignKey('Manufacturers', on_delete=models.PROTECT, verbose_name='Производитель')
    comment = models.TextField(verbose_name='Комментарий')

class Suppliers (models.Model):
    title = models.CharField (max_length=30, verbose_name = 'Наименование организации')
    INN = models.IntegerField (verbose_name = 'ИНН')
    CIO = models.IntegerField (verbose_name = 'КПП')
    FullNameManager = models.CharField (max_length = 150, verbose_name = 'ФИО руководителя')
    telephone = models.CharField (max_length = 20, verbose_name = 'Телефон')
    email = models.CharField (max_length = 30, verbose_name = 'Эл почта')

class Sales (models.Model):
    id_suppliers = models.ForeignKey('StoreDepartments', on_delete=models.PROTECT, verbose_name='Отдел магазина')
    id_autoParts = models.ForeignKey('AutoParts', on_delete=models.PROTECT, verbose_name='Автозапчасть')
    count = models.IntegerField(verbose_name='Количество')
    DateOfSale = models.DateField(verbose_name='Дата продажи')

class Roles (models.Model):
    role = models.CharField (max_length = 20, verbose_name = 'Роль')

class UserRoles (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    id_role = models.ForeignKey('Roles', on_delete=models.PROTECT, verbose_name='Роль')