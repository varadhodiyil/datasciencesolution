from __future__ import division
from datascience.core.classifiers.credit_analysis import CreditRiskAnalysis
from datascience.core.classifiers.credit_fraud import RandomForest , load_credit_fraud_Model
creditRisk = CreditRiskAnalysis()
from langdetect import detect_langs
from summarize import FrequencySummarizer
from datascience.core.serializers import ContactSerializer
from django.core.mail import EmailMessage
# fraud_detection  = RandomForest(classColumn="Class")
# fraud_detection.train()
# creditRisk.train()
fraud_detection = load_credit_fraud_Model()
def predict_credit_risk(data):
    return creditRisk.predict([data.values()])


def predict_fraud(data):
    return fraud_detection.predict([data.values()])

def lang_detect(data):
    data = data['text']
    return detect_langs(data)

def summarize_text(content):
    data=dict()
    try:
        fs = FrequencySummarizer()
        s_dict=fs.summarize(content, 2)
        summary=""
        for s in s_dict:
            summary=summary+s
        data['summary']=summary
        data['report']=dict()
        data['report']['original_length'] =len(content)
        data['report']['summary_length'] =len(summary)
        data['report']['ratio']=(100 - (100 *(len(summary) / len(content))))
    except AssertionError as e:
        raise e
        data['request']="Invalid Request"
    return data

def contact_form(data):
    s = ContactSerializer(data = data)
    resp = dict()
    if s.is_valid():
        title = "New Request from " + s.data['first_name']
        body = "Name : "+ s.data['first_name'] + s.data['last_name']+ \
                "\n\n Email : " +s.data['email']+ "\t Phone : "+s.data['phone'] + \
                "\n\n Company : " +s.data['company'] + \
                "\n\n\n\n\n\n Requirement :" + s.data['requirement']
        # to_email = ["ram@skalenow.com","sales@skalenow.com"]
        to_email = ['madhan_94@live.com']
        email = EmailMessage(title, body, to= to_email,from_email="Madhan <varadhodiyil@gmail.com>")
        email.send()
        resp['status'] = True
    else:
        resp['status'] = False
        resp['error'] =  s.errors
    return resp