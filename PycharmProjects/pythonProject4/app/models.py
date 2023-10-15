from django.db import models

class Cafe(models.Model):

    name = models.CharField('Name', max_length=256)
    descriptions = models.TextField('Description')

    def __str__(self):
        return f'{self.name}'
    
class Menu(models.Model):
    name = models.CharField('Name', max_length=256)
    image = models.ImageField('Image')
    cafe = models.ForeignKey(Cafe,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'
        
class Food(models.Model):
    
    name = models.CharField('Name', max_length=256)
    descriptions = models.TextField('Description')
    image = models.ImageField('Image')
    price = models.PositiveBigIntegerField('Price')
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'
    


class Client(models.Model):
    fulname = models.CharField('Fullname', max_length=256)
    telefon_number = models.PositiveBigIntegerField('Telefon_Number')

    def __str__(self):
        return f'{self.fulname}'
    
class Sponsor(models.Model):
    name = models.CharField('Fullname', max_length=256)
    image = models.ImageField('Image')

    def __str__(self):
        return f'{self.name}'

class Blog(models.Model):
    image = models.ImageField('Image')
    title = models.CharField('title',max_length=256)
    text = models.TextField('Description')
    data = models.DateTimeField('Data')

    