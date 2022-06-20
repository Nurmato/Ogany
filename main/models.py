from django.db import models

# Create your models here.
class Category5(models.Model):
    img = models.ImageField("Изображение", upload_to='upload/categories')
    name = models.CharField(max_length=100)
    price = models.IntegerField('Цена', default=0)


    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField("Название товара", max_length=255)
    price = models.IntegerField("Цена", default=0)
    category = models.ForeignKey(Category5, verbose_name="Категория", on_delete=models.CASCADE)
    description = models.CharField("Описание", max_length=255, default='', blank=True, null=True)
    image = models.ImageField("Изображение", upload_to='upload/products')


class Contact11(models.Model):
    name = models.CharField('Number', max_length=255)
    email = models.EmailField('Email почта')
    message = models.TextField('Message')
    sent_at = models.DateTimeField(auto_now_add=True)


class Subcribe(models.Model):
    email = models.EmailField('Email почта')
    sent_at = models.DateTimeField(auto_now_add=True)


class OrderData(models.Model):
    name = models.CharField('ФИО', max_length=255)
    number = models.CharField('Номер Телефона', max_length=255)
    email = models.EmailField('Email')
    address = models.CharField('Адрес', max_length=255)
    message = models.TextField('Сообщение')

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.CharField('Товар', max_length=255)
    price = models.IntegerField('Цена')
    count = models.IntegerField('Количество')
    total_sum = models.IntegerField('Общая сумма')
    customer = models.ForeignKey(OrderData, on_delete=models.CASCADE, verbose_name='Получатель')
    sent_at = models.DateTimeField('Время отправки', auto_now_add=True)

class Categories(models.Model):
    img = models.ImageField("Изображение", upload_to='upload/categories1')
    name = models.CharField(max_length=100)