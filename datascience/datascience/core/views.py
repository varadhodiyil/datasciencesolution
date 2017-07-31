# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.parsers import JSONParser, FormParser
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.response import Response
from datascience.core.resources import predict_credit_risk , predict_fraud
# Create your views here.
credit_data = [
            {
                "type": "RevolvingUtilizationOfUnsecuredLines" , "min":"0" , "max":"1" , "step":"0.01","val":0.05
            },
            {
                "type": "Age" , "min":"18" , "max":"80" , "step":"1" , "val":30
            },
            {
                "type": "Days59PastDueNotWorse" , "min":"0" , "max":"1000" , "step":"1","val" : 25
            },
            {
                "type": "DebtRatio" , "min":"0" , "max":"1" , "step":"0.01" , "val" : 0.25
            },
            {
                "type": "MonthlyIncome" , "min":"100" , "max":"100000000" , "step":"50" , "val":2500
            },
            {
                "type": "NumberOfOpenCreditLinesAndLoans" , "min":"0" , "max":"1000" , "step":"1","val" : 80
            },
            {
                "type": "NumberOfTimes90DaysLate" , "min":"0" , "max":"1000" , "step":"1","val" : 70
            },
            {
                "type": "NumberRealEstateLoansOrLines" , "min":"0" , "max":"1000" , "step":"1", "val" : 10
            },
            {
                "type": "NumberOfTime60To89DaysPastDueNotWorse" , "min":"0" , "max":"1000" , "step":"1" ,"val" : 125
            },
            {
                "type": "NumberOfDependents" , "min":"0" , "max":"10" , "step":"1" ,"val" : 2
            }]

def home(request):
    return render(request,"index.html")


@api_view(['POST'])
def creditPredict(request):
    data = request.data
    resp = dict()
    if len(data) == len(credit_data):

        resp = predict_credit_risk(data)
    else:
        print "no data lol"
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

def clv(request):
    return render(request,"clv.html")

def loyalty(request):
    return render(request,"customer_loyalty.html")

def churn(request):
    return render(request , "retention.html")

@api_view(["GET","POST"])
@parser_classes((JSONParser,FormParser))
def fraudDetection(request):
    labels = [
                {
                    "value": 0, 
                    "label": "Time"
                }, 
                {
                    "value": -1.3598071336738, 
                    "label": "V1"
                }, 
                {
                    "value": -0.07278117330985, 
                    "label": "V2"
                }, 
                {
                    "value": 2.53634673796914, 
                    "label": "V3"
                }, 
                {
                    "value": 1.37815522427443, 
                    "label": "V4"
                }, 
                {
                    "value": -0.338320769942518, 
                    "label": "V5"
                }, 
                {
                    "value": 0.462387777762292, 
                    "label": "V6"
                }, 
                {
                    "value": 0.239598554061257, 
                    "label": "V7"
                }, 
                {
                    "value": 0.098697901261051, 
                    "label": "V8"
                }, 
                {
                    "value": 0.363786969611213, 
                    "label": "V9"
                }, 
                {
                    "value": 0.090794171978932, 
                    "label": "V10"
                }, 
                {
                    "value": -0.551599533260813, 
                    "label": "V11"
                }, 
                {
                    "value": -0.617800855762348, 
                    "label": "V12"
                }, 
                {
                    "value": -0.991389847235408, 
                    "label": "V13"
                }, 
                {
                    "value": -0.311169353699879, 
                    "label": "V14"
                }, 
                {
                    "value": 1.46817697209427, 
                    "label": "V15"
                }, 
                {
                    "value": -0.470400525259478, 
                    "label": "V16"
                }, 
                {
                    "value": 0.207971241929242, 
                    "label": "V17"
                }, 
                {
                    "value": 0.025790580198559, 
                    "label": "V18"
                }, 
                {
                    "value": 0.403992960255733, 
                    "label": "V19"
                }, 
                {
                    "value": 0.251412098239705, 
                    "label": "V20"
                }, 
                {
                    "value": -0.018306777944153, 
                    "label": "V21"
                }, 
                {
                    "value": 0.277837575558899, 
                    "label": "V22"
                }, 
                {
                    "value": -0.110473910188767, 
                    "label": "V23"
                }, 
                {
                    "value": 0.066928074914673, 
                    "label": "V24"
                }, 
                {
                    "value": 0.128539358273528, 
                    "label": "V25"
                }, 
                {
                    "value": -0.189114843888824, 
                    "label": "V26"
                }, 
                {
                    "value": 0.133558376740387, 
                    "label": "V27"
                }, 
                {
                    "value": -0.021053053453822, 
                    "label": "V28"
                }, 
                {
                    "value": 149.62, 
                    "label": "Amount"
                }
            ]
    resp = dict()
    resp['labels'] = labels
    if request.method == "POST":
        data = request.data
        resp = predict_fraud(data)
        return Response(resp)
    return render(request, "fraud-detection.html",resp)