from django.shortcuts import render
from django.views import generic
from .models import Stol,CurrentDate,MonthJournal
from datetime import datetime,date,timedelta
from django.views.generic.base import TemplateView
from django.shortcuts import render
from calendar import monthrange, weekday, day_abbr
from django.urls import reverse






# Create your views here.

class DateView(TemplateView):
     template_name = 'Zakaz/date.html'

     def get_context_data(self, **kwargs):
         # get context data from TemplateView class
         context = super(DateView, self).get_context_data(**kwargs)
         today = datetime.today()
         day = date(today.year,today.month,today.day)

         first_day = day
         cur_day = first_day
         next_day = day + timedelta(days=1)
         prev_day = day + timedelta(days=-1)
         last_day = first_day + timedelta(days=15)

         def chislo(request):
             if request.method == 'POST':
                 q=request.POST.get('inputDate')
                 cur_day=q
             return cur_day


         context['prev_day'] = prev_day.strftime('%d/%m/%Y')
         context['next_day'] = next_day.strftime('%d/%m/%Y')
         context['cur_day'] = cur_day.strftime('%d/%m/%Y')
         context['first_day'] = first_day.strftime('%d/%m/%Y')
         context['last_day'] = last_day.strftime('%d/%m/%Y')

         context['Stol']=Stol.objects.all()

         return context

class JournalView(TemplateView):
     template_name = 'Zakaz/journal.html'

     def get_context_data(self, **kwargs):
         # get context data from TemplateView class
         context = super(JournalView, self).get_context_data(**kwargs)

         # перевіряємо чи передали нам місяць в параметрі,
         # якщо ні - вичисляємо поточний;
         # поки що ми віддаємо лише поточний:
         today = datetime.today()
         month = date(today.year, today.month, 1)

         context['day']=MonthJournal.objects.all()

         # обчислюємо поточний рік, попередній і наступний місяці
         # а поки прибиваємо їх статично:
         context['prev_month'] = '2014-06-01'
         context['next_month'] = '2014-08-01'
         context['year'] = 2014

          # також поточний місяць;
         # змінну cur_month ми використовуватимемо пізніше
         # в пагінації; а month_verbose в
         # навігації помісячній:
         context['cur_month'] = '2014-07-01'
         context['month_verbose'] = u"Липень"

         # тут будемо обчислювати список днів у місяці,
         # а поки заб'ємо статично:
         context['month_header'] = [
             {'day': 1, 'verbose': 'Пн'},
             {'day': 2, 'verbose': 'Вт'},
             {'day': 3, 'verbose': 'Cр'},
             {'day': 4, 'verbose': 'Чт'},
             {'day': 5, 'verbose': 'Пт'}]

         # витягуємо усіх студентів посортованих по
         queryset = Stol.objects.order_by('title')

         # це адреса для посту AJAX запиту, як бачите, ми
         # робитимемо його на цю ж в'юшку; в'юшка журналу
         # буде і показувати журнал і обслуговувати запити
         # типу пост на оновлення журналу;
         update_url = reverse('journal')

         # пробігаємось по усіх студентах і збираємо
         # необхідні дані:
         stols = []
         for stol in queryset:
             # TODO: витягуємо журнал для студента і
             #       вибраного місяця

             # набиваємо дні для студента
             days = []
             for day in range(1, 31):
                 days.append({
                     'day': day,
                     'present': True,
                     'date': date(2014, 7, day).strftime(
                         '%Y-%m-%d'),
                 })

             # набиваємо усі решту даних студента
             stols.append({
                 'fullname': u' %s' % (stol.title),
                 'days': days,
                 'id': stol.id,
                 'update_url': update_url,
                              })

         # застосовуємо піганацію до списку студентів


         # повертаємо оновлений словник із даними
         return context
