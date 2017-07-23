# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.parsers import JSONParser, FormParser
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.response import Response
from datascience.core.resources import predict_credit_risk
# Create your views here.
credit_data = [{
                "type": "RevolvingUtilizationOfUnsecuredLines" , "min":"0" , "max":"1" , "step":"0.1"
            },
            {
                "type": "Age" , "min":"18" , "max":"80" , "step":"1"
            },
            {
                "type": "Days59PastDueNotWorse" , "min":"0" , "max":"1000" , "step":"1"
            },
            {
                "type": "DebtRatio" , "min":"0" , "max":"1" , "step":"0.01"
            },
            {
                "type": "MonthlyIncome" , "min":"100" , "max":"100000000" , "step":"50"
            },
            {
                "type": "NumberOfOpenCreditLinesAndLoans" , "min":"0" , "max":"1000" , "step":"1"
            },
            {
                "type": "NumberOfTimes90DaysLate" , "min":"0" , "max":"1000" , "step":"1"
            },
            {
                "type": "NumberRealEstateLoansOrLines" , "min":"0" , "max":"1000" , "step":"1"
            },
            {
                "type": "NumberOfTime60To89DaysPastDueNotWorse" , "min":"0" , "max":"1000" , "step":"1"
            },
            {
                "type": "NumberOfDependents" , "min":"0" , "max":"10" , "step":"1"
            }]

def home(request):
    return render(request,"index.html")


@api_view(['POST'])
def creditPredict(request):
    data = request.data
    resp = dict()
    if len(data) == len(credit_data):
        
        resp = predict_credit_risk(data)
    return Response(resp)

def creditAnalyis(request):
    resp = dict()

    resp['labels']  = credit_data
    return render(request,"credit-analysis.html" , resp)

def summarize(request):
    return render(request,"summarizer.html")

def ner(request):
    return render(request,"ner.html")

def sentiment(request):
    return render(request,"sentiment.html")

def langdetect(request):
    return render(request,"langdetect.html")