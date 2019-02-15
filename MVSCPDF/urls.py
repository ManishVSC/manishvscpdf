"""MVSCPDF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from .import views
from django_pdfkit import PDFView


urlpatterns = [
    path('', views.welcome),
    path('home', views.home),
    path('moneygram', views.moneygram),
    path('admin/', admin.site.urls),


    path('agreementform', views.agreementform), # Loan Agreement Form
    path('agreement', views.agreement), #Loan Agreement BackEnd



    path('westernform', views.westernform), #Western Union Form
    path('western', views.western), #Western Union BackEnd

    path('loantaxform', views.loantaxform), #Western Union BackEnd
    path('loantax', views.loantax), #Western Union BackEnd


    path('moneygramform', views.western), #Western Union BackEnd
    path('moneygram', views.western), #Western Union BackEnd


    path('outstandingform', views.outstandingform), #Western Union BackEnd
    path('outstanding', views.outstanding), #Western Union BackEnd


    path('remainoutstandingform', views.remainoutstandingform), #Western Union BackEnd
    path('remainoutstanding', views.remainoutstanding), #Western Union BackEnd


    path('filechargesform', views.filechargesform), #Western Union BackEnd
    path('filecharges', views.filecharges), #Western Union BackEnd

    path('counter', views.counter),

    path('login', views.login),

]
