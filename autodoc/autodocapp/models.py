from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    surname = models.CharField(max_length=30, verbose_name='Фамилия')
    last_name = models.CharField(max_length=30, verbose_name='Отчество')
    birth_date = models.DateField(verbose_name='Дата рождения', null=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фотография')


class Brands(models.Model):
    brand = models.CharField(max_length=50, verbose_name='Марка автозапчасти')

    def __str__(self):
        return self.brand

    def get_absolute_url(self):
        return f'autodocapp/marks.html'

class Models (models.Model):
    model = models.CharField(max_length=50, verbose_name='Модель марки')

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return f'autodocapp/models.html'


class BrandsAndModels (models.Model):
    id_brand = models.ForeignKey('Brands', on_delete=models.CASCADE, verbose_name='Марка автомобиля')
    id_model = models.ForeignKey('Models', on_delete=models.CASCADE, verbose_name='Модель')


class Cities (models.Model):
    city = models.CharField(max_length=50, verbose_name='Город')

    def __str__(self):
        return self.city


class Streets (models.Model):
    street = models.CharField(max_length=50, verbose_name='Улица')

    def __str__(self):
        return self.street


class Manufacturers (models.Model):
    manufacturer = models.CharField(max_length=50, verbose_name='Производитель')


class StoreDepartments (models.Model):
    id_city = models.ForeignKey('Cities', on_delete=models.PROTECT, verbose_name='Город')
    id_street = models.ForeignKey('Streets', on_delete=models.PROTECT, verbose_name='Улица')
    house = models.CharField(max_length=10, verbose_name = 'Дом')
    telephone = models.CharField(max_length=20, verbose_name = 'Телефон')

    def __str__(self):
        return (self.id_city.city, self.id_street.street)


class AutoParts (models.Model):
    vendor_code = models.CharField(max_length=20, verbose_name='Артикул')
    name = models.CharField(max_length=20, verbose_name='Наименование')
    id_brand_and_models = models.ForeignKey('BrandsAndModels', on_delete=models.PROTECT, verbose_name='Автомобиль')
    id_manufacturer = models.ForeignKey('Manufacturers', on_delete=models.PROTECT, verbose_name='Производитель')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    comment = models.TextField(verbose_name='Комментарий')


class AutoPartsInStock (models.Model):
    id_StoreDepartment = models.ForeignKey('StoreDepartments', on_delete=models.PROTECT, verbose_name='Магазин')
    id_AutoParts = models.ForeignKey('AutoParts', on_delete=models.PROTECT, verbose_name='Автозапчасть')
    price = models.FloatField(verbose_name="Цена")
    amount = models.IntegerField(verbose_name="Количество")


class Suppliers (models.Model):
    title = models.CharField (max_length=30, verbose_name='Наименование организации')
    INN = models.IntegerField (verbose_name='ИНН')
    CIO = models.IntegerField (verbose_name='КПП')
    FullNameManager = models.CharField (max_length=150, verbose_name = 'ФИО руководителя')
    telephone = models.CharField (max_length=20, verbose_name='Телефон')
    email = models.CharField (max_length=30, verbose_name='Эл почта')


class Supply(models.Model):
    id_supplier = models.ForeignKey('Suppliers', on_delete=models.PROTECT, verbose_name='Поставщик')
    id_AutoParts = models.ForeignKey('AutoParts', on_delete=models.PROTECT, verbose_name='Автозапчасть')
    purchase_price = models.FloatField(verbose_name='Цена закупки')
    quantity = models.IntegerField(verbose_name='Количество')
    delivery_date = models.DateField(verbose_name='Дата поступления')

class Sales (models.Model):
    id_suppliers = models.ForeignKey('StoreDepartments', on_delete=models.PROTECT, verbose_name='Отдел магазина')
    id_autoParts = models.ForeignKey('AutoParts', on_delete=models.PROTECT, verbose_name='Автозапчасть')
    count = models.IntegerField(verbose_name='Количество')
    DateOfSale = models.DateField(verbose_name='Дата продажи')
