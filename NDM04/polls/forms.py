# Listing 6.1
from django import forms



class UserForm1(forms.Form): #rgd01

    k = forms.FloatField(label="Введите K,мм (например, 0.3)")   
    Ф = forms.FloatField(label="Введите Ф,мм (например, 2.5)")   
    D = forms.IntegerField(label="Введите D,мм (например, 200)")   
    d = forms.IntegerField(label="Введите d,мм (например, 180)")   

    
class UserForm2(forms.Form): #панорама

    k = forms.FloatField(label="Введите k,мм (например, 0.3)")   
    Ф = forms.FloatField(label="Введите Ф,мм (например, 2.5)")   
    D = forms.IntegerField(label="Введите D,мм (например, 200)")   
    dвн = forms.IntegerField(label="Введите d,мм (например, 180)") 
    h_усил_шва = forms.FloatField(label="Введите h,(например, 1.5)")

class UserForm3(forms.Form):

    #источник = forms.ChoiceField(label="Укажите тип источника",
                             #choices=(("Иридий-192","Иридий-192" ),
                                      #("Кобальт-60","Кобальт-60" )))

    активность0 = forms.IntegerField(label="Укажите активность источника на дату зарядки источника, Ku")   
    дата0 = forms.DateField(label="Укажите дату зарядки источника - дата0(дд/мм/гг)")   
    дата1 = forms.DateField(label="Укажите дату экспозиции дата1(дд/мм/гг)")    

class UserForm4(forms.Form):

    H01 = forms.FloatField(label="Введите H,мм (например, 20)")   
    B01 = forms.FloatField(label="Введите B,мм (например, 7)")   
    alfa01 = forms.IntegerField(label="Введите alfa,град. (например, 70)")   
    b01 = forms.FloatField(label="Введите b,мм (например, 20)") 
