"""datascience URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url ,include
from datascience.core import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^credit/$', views.creditAnalyis ,name="credit-analysis"),
    url(r'^credit/predit/$', views.creditPredict ,name="credit-predit"),
    url(r'^summarize/$',views.summarize,name="summarize"),
    url(r'^ner/$',views.ner,name="ner"),
    url(r'^sentiment/$',views.sentiment,name="sentiment"),
    url(r'^langdect/$',views.langdetect,name="langdect"),
    url(r'^clv/$',views.clv,name="clv"),
    url(r'^loyalty/$',views.loyalty,name="loyalty"),
    url(r'^churn/$',views.churn,name="churn"),
    url(r'fraud-detection/$',views.fraudDetection , name= "fraud-detection"),
    url(r'contact/$' , views.send_email , name="contact"),
    url(r'satisfaction/$' , views.satisfaction , name="satisfaction")
]
