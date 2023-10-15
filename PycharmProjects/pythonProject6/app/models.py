from django.db import models

class Event(models.Model):

    title = models.CharField('имя события', max_length=256, default='событие')
    description = models.TextField('oписание события', blank=True , null=True)
    date = models.DateField('Дата события', auto_now=True)
    is_important = models.BooleanField('важность события', default=False)
    image = models.ImageField('фото события', upload_to='event-image')

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'сoбытия'
        verbose_name_plural = 'событие'


        