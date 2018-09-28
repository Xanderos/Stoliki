from django.db import models
from datetime import datetime

# Create your models here.
class Stol(models.Model):

    title = models.IntegerField(default=1)
    quantity = models.IntegerField(default=1)
    forma = models.CharField(max_length=20,default='square')
    x_cord = models.IntegerField(default=1)
    y_cord = models.IntegerField(default=1)
    len_stol = models.FloatField(default=1)
    width_stol = models.FloatField(default=1)
    reserved = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Stol'
        verbose_name_plural = "Stoliki"

    def __str__(self):
        return str(self.title)


class CurrentDate(models.Model):
     """current date"""

     class Meta:
         verbose_name = u'Текущая дата'

     date = models.DateField(
         verbose_name=u'Дата',
         blank=False)

     def __str__(self):
         return u'%d, %d, %d' % (self.date.day,self.date.month,self.date.year)

class MonthJournal(models.Model):


     class Meta:
         verbose_name = u' Журнал'
         verbose_name_plural = u'Журнал'

     stol = models.ForeignKey('Stol',
         verbose_name=u'Stol',
         blank=False,
         on_delete=models.CASCADE)

     # we only need year and month, so always set day to first day of the month
     date = models.DateField(
         verbose_name=u'Дата',
         blank=False)

     def __str__(self):
         return u'%s:%d, %d, %d' % (self.stol.title,self.date.day, self.date.month,
             self.date.year)



# Create your models here.
