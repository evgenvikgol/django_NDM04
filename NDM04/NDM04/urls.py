"""NDM04 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from django.urls import re_path
from polls import views
from django.views.generic import TemplateView
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    url(r'^rgd/$', views.rgd, name='rgd'), 
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^tema01/$', views.tema01, name='tema01'),    
    path('панорама', views.панорама), # 
    path('активность', views.активность),  
    path('узд01', views.узд01),      

]

    #path('rgd01', views.rgd01),  
    #url(r'^polls/rgd01/$', views.rgd, name='rgd01'),
    #url(r'^polls/панорама01/$', views.панорама, name='ПанорамаРГД'),  
    #url(r'^polls/активность01/$', views.активность, name='активность'), 
    
    #path('about/', views.about),
    #path('contact/', views.contact),
    #path('панорама', views.панорама), # 
    #path('активность', views.активность), 
    #path('rgd01', views.rgd01),     
    #path('радиография01/', views.радиография01), # 
     

    #path('ргд/', include('ргд.urls')),
    #path('узд/', include('узд.urls')),

 


    #url(r'^rgd/$', views.rgd, name='rgd'),
    #url(r'^books/$', views.BookListView.as_view(), name='books'),
    #url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    #url(r'^authors/$', views.AuthorListView.as_view(), name='authors'), 

    #url(r'^usd/$', views.usd, name='usd'),
    #url(r'^t_metr/$', views.t_metr, name='t_metr'),
    #url(r'^sp1/$', views.sp1, name='sp1'),    