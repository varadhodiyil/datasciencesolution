# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.mail import send_mail
from django.shortcuts import render
from rest_framework.parsers import JSONParser, FormParser
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.response import Response
from datascience.core.resources import predict_credit_risk , predict_fraud , lang_detect , summarize_text ,contact_form
from rest_framework import status
import json 
import os
# Create 
# your views here.
credit_data = [
    {
        "val": 0.05, 
        "min": "0", 
        "max": "1", 
        "value": "RevolvingUtilizationOfUnsecuredLines", 
        "step": "0.01", 
        "type": "RevolvingUtilizationOfUnsecuredLines"
    }, 
    {
        "val": 30, 
        "min": "18", 
        "max": "80", 
        "value": "Age", 
        "step": "1", 
        "type": "Age"
    }, 
    {
        "val": 25, 
        "min": "0", 
        "max": "1000", 
        "value": "Days59PastDueNotWorse", 
        "step": "1", 
        "type": "Days59PastDueNotWorse"
    }, 
    {
        "val": 0.25, 
        "min": "0", 
        "max": "1", 
        "value": "DebtRatio", 
        "step": "0.01", 
        "type": "DebtRatio"
    }, 
    {
        "val": 2500, 
        "min": "100", 
        "max": "100000000", 
        "value": "MonthlyIncome", 
        "step": "50", 
        "type": "MonthlyIncome"
    }, 
    {
        "val": 80, 
        "min": "0", 
        "max": "1000", 
        "value": "NumberOfOpenCreditLinesAndLoans", 
        "step": "1", 
        "type": "NumberOfOpenCreditLinesAndLoans"
    }, 
    {
        "val": 70, 
        "min": "0", 
        "max": "1000", 
        "value": "Number Of Times 90Days Late", 
        "step": "1", 
        "type": "NumberOfTimes90DaysLate"
    }, 
    {
        "val": 10, 
        "min": "0", 
        "max": "1000", 
        "value": "Number Real Estate Loans Or Lines", 
        "step": "1", 
        "type": "NumberRealEstateLoansOrLines"
    }, 
    {
        "val": 125, 
        "min": "0", 
        "max": "1000", 
        "value": "Number Of Time 60-89 Days Past Due Not Worse", 
        "step": "1", 
        "type": "NumberOfTime60To89DaysPastDueNotWorse"
    }, 
    {
        "val": 2, 
        "min": "0", 
        "max": "10", 
        "value": "Number Of Dependents", 
        "step": "1", 
        "type": "NumberOfDependents"
    }
]
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

@api_view(["GET","POST"])
@parser_classes((JSONParser,FormParser))
def summarize(request):
    if request.method == "GET":
        return render(request,"summarizer.html")
    if request.method == "POST":
        data = request.data
        resp = dict()
        resp['status'] = False
        resp['message'] = " Invalid Request"
        if "data" in  data:
            resp = summarize_text(data['data'])
            return Response(resp,status=status.HTTP_200_OK)
        return Response(resp , status=status.HTTP_400_BAD_REQUEST)

def ner(request):
    return render(request,"ner.html")

def sentiment(request):
    return render(request,"sentiment.html")

@api_view(["GET","POST"])
@parser_classes((JSONParser,FormParser))
def langdetect(request):
    if request.method == "POST":
        data = request.data
        r = lang_detect(data)
        resp = list()
        for l in r:
            resp.append(l.__dict__)
        return Response(resp)
    return render(request,"langdetect.html")

def clv(request):
    return render(request,"clv.html")

def loyalty(request):
    return render(request,"customer_loyalty.html")

def churn(request):
    return render(request , "retention.html")

def satisfaction(request):
    return render(request , "satisfaction.html")

def recommender(request):
    return render(request , "food-recommendation.html")

def recommender_product(request):
    return render(request , "recommender-product.html")

def claim_predict(request):
    labels = [
               {
                    "value":6.43,
                    "model":"veh_value",
                    "label":"Vehicle Value"
                },
                {
                    "value":0.241897754,
                    "model":"exposure",
                    "label" : "Exposure"
                },
                {
                    "value":"STNWG",
                    "model":"veh_body",
                    "label":"Vehicle Body"
                },
                {
                    "value":"M" ,
                    "model":"veh_age",
                    "label":"Vehicle Age"
                },
                {
                    "value":0,
                    "model":"gender",
                    "label":"Gender"
                },
                {
                    "value":"A",
                    "model":"area",
                    "label":"Area"
                },
                {
                    "value":3,
                    "model":"dr_age",
                    "label":"DR Age"
                },
                {
                    "value":0,
                    "model":"claim_ind",
                    "label":"Claim Ind."
                },
                {
                    "value":0,
                    "model":"claim_count",
                    "label":"Claim Count"
                },
            ]
    data = dict()
    data['labels'] = labels
    return render(request , "claim-predict.html" , data )

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
@api_view(['post'])
def contact(request):
    # status = send_mail(
    # 'Subject here',
    # 'Here is the message.',
    # 'varadhodiyil@gmail.com',
    # ['madhan_94@live.com'],
    # )
    status = contact_form(request.data)
    

    return Response(status)

def click_stream(request):
    return render(request,"click-stream.html")

@api_view(["GET"])
def click_stream_data(request):
    path = os.path.dirname(__file__)
    data = json.load(open(path+"/data.json","r"))
    return Response(data)