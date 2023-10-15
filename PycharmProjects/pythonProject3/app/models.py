from re import M
from tabnanny import verbose
from django.db import models

class Product(models.Model):

    name = models.CharField('имя продукта',max_length=256)
    description = models.TextField('описание продукта')
    price = models.PositiveIntegerField('цена продукта')

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name ='продукт'
        verbose_name_plural = 'продукты'