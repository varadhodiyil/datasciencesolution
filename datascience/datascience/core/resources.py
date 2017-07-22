from datascience.core.classifiers.credit_analysis import CreditRiskAnalysis

creditRisk = CreditRiskAnalysis()
# creditRisk.train()
def predict_credit_risk(data):
    return creditRisk.predict([data.values()])