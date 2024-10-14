from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from.models import Вопрос
from django.template import loader
from django.views import generic
import requests
from.forms import UserForm1
from.forms import UserForm2
from.forms import UserForm3
from.forms import UserForm4

import datetime as dt
from bs4 import BeautifulSoup # Модуль для работы с HTML
import math

def index0(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def detail(request, Вопрос_id):
    return HttpResponse("Вы смотрите на вопрос %s." % Вопрос_id)
def results(request, Вопрос_id):
    response = " Вы просматриваете результаты опроса %s."
    return HttpResponse(response % Вопрос_id)
def vote(request, Вопрос_id):
    return HttpResponse("Вы голосуете по вопросу %s." % Вопрос_id)





def index(request):
    latest_Вопрос_list = Вопрос.objects.order_by('-pub_date')[:5]
    context = {'latest_Вопрос_list': latest_Вопрос_list}
    return render(request, 'polls/index.html', context)




#class BookListView(generic.ListView):
    #model = Book
    
 # Listing 9.14
#class BookDetailView(generic.DetailView):
    #model = Book

# Listing 9.19
#class AuthorListView(generic.ListView):
    #model = Author
    #paginate_by = 4


def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")
    
def tema01(request):
    return render(request, "tema01.html")    
    

def rgd01(k,Ф,D,d):
      k=float(k)
      Ф=float(Ф)
      D=int(D)
      d=int(d)


      if Ф/k>=2 :
            c=2*Ф/k
      else:
           c=4

      L =  int(0.8*c*(D - d))
      Фk=int(Ф/k*10) /10
      return f" L(минимальная длина снимка для схемы рис. 3а) =  {L}  mm, f - минимальное фокусное расстояние для рис.3а = {int(0.7*c*(D - d))} mm, f - минимальное фокусное расстояние для рис.3б = {int(0.5*c*D)} mm "

def rgd(request):
    if request.method == "POST":
        k = request.POST.get("k")  # получить значения поля источник
        Ф = request.POST.get("Ф")    
        D = request.POST.get("D") 
        d = request.POST.get("d")    
   
        yyy=rgd01(k,Ф,D,d)
        output = "<h2>ГОСТ Р 50.05.07—2018 рис.3а и рис.2б</h2><h3> Исходные данные:<br> k - чувствительность - {0} мм<br> Ф - фокусное пятно - {1} мм <br> D - наружный диаметр - {2} мм<br> d - внутренний диаметр - {3} мм <br>Результат:<br> {4} </h3>".format(k,Ф,D,d,yyy )        
        return HttpResponse(output)
    else:
        userform = UserForm1()
    return render(request, "polls/rgd01.html", {"form": userform})      

def ПанорамаРГД(h_усил_шва,Ф,D,dвн,k):
    k=float(k)
    Ф=float(Ф)
    D=int(D)
    dвн=int(dвн)
    h_усил_шва=float(h_усил_шва)
    f = dвн / 2
    m = int(dвн / D*100)/100
    Sрад = (D - dвн) / 2 + h_усил_шва
    Фкрит = int(k * dвн / (D - dвн)*100)/100

    if Фкрит>=Ф :
        return f" Фкрит = {Фкрит} мм,  f = {f} мм"
    else:
        return f" Фкрит = {Фкрит} мм.  Выберите источник излучения с меньшим фокусным пятном!"




def панорама(request):
    if request.method == "POST":
        k = request.POST.get("k")  # получить значения поля источник
        Ф = request.POST.get("Ф")    
        D = request.POST.get("D")  # получить значения поля источник
        dвн = request.POST.get("dвн")    
        h_усил_шва = request.POST.get("h_усил_шва")   
        yyy=ПанорамаРГД(h_усил_шва,Ф,D,dвн,k)
        output = "<h2>ГОСТ Р 50.05.07—2018 рис 3е</h2><h3>Исходные данные:<br> h - усиление шва = {0} мм, <br> k - чувствительность = {4} мм <br> Ф - фокусное пятно = {1} мм <br> D - наружный диаметр - {2} мм <br> d - внутренний диаметр = {3} мм <br> Результат: {5} </h3>".format(h_усил_шва,Ф,D,dвн,k,yyy )        
        return HttpResponse(output)
    else:
        userform = UserForm2()
    return render(request, "polls/панорама01.html", {"form": userform})      



def akt_istoch( активность0,дата0,дата1):

    date_obj0 = dt.datetime.strptime(дата0,'%d/%m/%y')
    #print(date_obj0)
    date_obj1 = dt.datetime.strptime(дата1,'%d/%m/%y')
    #print(date_obj1)

    дельта0=date_obj1-date_obj0
    дельта=str(дельта0)
    #print(дельта)

    num_m=дельта.find("d")  #206 days, 0:00:00
    delta1=дельта[0:num_m-1]

    Q1 = int(активность0) * math.exp(-int(delta1) / 106.9)
    #print(f'С момента зарядки - {дата0}- источника прошло  {delta1} дней.    Первоначально источник был заряжен  до {активность0} кюри, сегодня его активность составляет  {int(Q1*10)/10} кюри')
    return f'С момента зарядки - {дата0}- источника прошло  {delta1} дней.    Первоначально источник был заряжен  до {активность0} кюри, сегодня его активность составляет  {int(Q1*10)/10} кюри'

def активность(request):
    if request.method == "POST":
        источник = request.POST.get("источник")  # получить значения поля источник
        пленка = request.POST.get("пленка")  # получить значения поля источник   
        активность0 = request.POST.get("активность0")  # получить значения поля источник         
        дата0 = request.POST.get("дата0")  # получить значения поля источник           
        дата1 = request.POST.get("дата1")  # получить значения поля источник           
        yyy=akt_istoch(активность0,дата0,дата1)
        output = "<h2>Активность источника излучений</h2><h3> Исходные требования:<br> - выбранная марка источника излучений: Иридий-192;<br> - активность источника на дату зарядки источника, Ku:  {1} ;<br> - начальная дата - {3};<br> - конечная дата: - {4};<br> Результат:<br>{5} </h3>".format(источник,активность0,пленка,дата0,дата1,yyy)        
        return HttpResponse(output)
    else:
        userform = UserForm3()
    return render(request, "polls/активность01.html", {"form": userform})    

def uzd01(H01,alfa01,B01,b01):
    H01=float(H01)
    B01=float(B01)
    alfa01=int(alfa01)
    b01=float(b01)
    L01=(H01*math.tan(alfa01*3.14/180)+B01+b01+5)

    return f"  {int(L01*10)/10}"


def узд01(request):
    if request.method == "POST":
        H01 = request.POST.get("H01")  # получить значения поля источник
        B01 = request.POST.get("B01")    
        alfa01 = request.POST.get("alfa01")  # получить значения поля источник
        b01 = request.POST.get("b01")    

        yyy=uzd01(H01,alfa01,B01,b01)
        output = "<h2>ГОСТ Р 50.05.02—2018 п.6.8.6</h2><h3> Исходные требования:<br> Н - номинальная толщина трубы = {0} мм, <br> aльфа - угол ввода, град. = {1}<br> B - полуширина усиления шва = {2} <br> b - ширина околошовной зоны = {3}<br><br> Результат: <br> Длина L цилиндрической части расточки (L= Htga+b+В+5 мм) должна быть не менее  {4} мм </h3>".format(H01,alfa01,B01,b01,yyy )        
        return HttpResponse(output)
    else:
        userform = UserForm4()
    return render(request, "polls/uzd01.html", {"form": userform})      

