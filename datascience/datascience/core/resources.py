from datascience.core.classifiers.credit_analysis import CreditRiskAnalysis
from datascience.core.classifiers.credit_fraud import RandomForest , load_credit_fraud_Model
creditRisk = CreditRiskAnalysis()
# fraud_detection  = RandomForest(classColumn="Class")
# fraud_detection.train()
# creditRisk.train()
fraud_detection = load_credit_fraud_Model()
def predict_credit_risk(data):
    return creditRisk.predict([data.values()])


def predict_fraud(data):
    return fraud_detection.predict([data.values()])