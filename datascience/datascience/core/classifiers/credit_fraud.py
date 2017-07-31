import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from datetime import datetime
import pickle



CREDIT_FRAUD_PICKLE =  os.path.join(os.path.dirname(__file__),"classified/credit_fraud.pickle")
print CREDIT_FRAUD_PICKLE
class RandomForest():

    def __init__(self,trainFile="creditcard.csv",classColumn=""):
        self.trainFile = os.path.join(os.path.dirname(__file__),trainFile)
        self.classColumn = classColumn
        self.classifier = None
        self.pickle_file = CREDIT_FRAUD_PICKLE

    def readData(self):
        data = pd.read_csv(self.trainFile)
        data_class_outcomes = data[self.classColumn]
        data.drop([self.classColumn], axis = 1, inplace = True)
        self.X_train = data
        self.y_train = data_class_outcomes
        
    def train(self,n_estimators=100):
        """
        This function fits and transforms data using 
        Random Forest Classifier  and 
        pickles the classifier
        """

        start = datetime.now()
        print "start" , start
        self.readData()
        clf_B = RandomForestClassifier(n_estimators=n_estimators)
        clf_B.fit(self.X_train, self.y_train)
        self.classiferModel =  clf_B

        with open(self.pickle_file,"wb") as h :
            pickle.dump(self,h)
            h.close()
        end = datetime.now()
        print "end" , end
        print "pickled at :", self.pickle_file
        print (end-start)


    def predict(self,dataset):
        # if self.classifier is None:
        #     self.loadModel()
        print self.classiferModel.predict(dataset)

def load_credit_fraud_Model():
    if os.path.exists(CREDIT_FRAUD_PICKLE):
        print "exists"
        classifier=pickle.load(open(CREDIT_FRAUD_PICKLE,'rb'))
        print "Loaded"
        return classifier
    else:
        print "unable to load Train file .. ! have you trained the model yet?"
        
# r = load_credit_fraud_Model()
# if r is not None:
#     test = [[0,-1.3598071336738,-0.07278117330985,2.53634673796914,1.37815522427443,-0.338320769942518,0.462387777762292,0.239598554061257,0.098697901261051,0.363786969611213,0.090794171978932,-0.551599533260813,-0.617800855762348,-0.991389847235408,-0.311169353699879,1.46817697209427,-0.470400525259478,0.207971241929242,0.025790580198559,0.403992960255733,0.251412098239705,-0.018306777944153,0.277837575558899,-0.110473910188767,0.066928074914673,0.128539358273528,-0.189114843888824,0.133558376740387,-0.021053053453822,149.62],
#             [4462,-2.30334956758553,1.759247460267,-0.359744743330052,2.33024305053917,-0.821628328375422,-0.07578757061946,0.562319782266954,-0.399146578487216,-0.238253367661746,-1.52541162656194,2.03291215755072,-6.56012429505962,0.022937323489096,-1.47010153611197,-0.698826068579047,-2.28219382856251,-4.78183085597533,-2.61566494476124,-1.33444106667307,-0.430021867171611,-0.294166317554753,-0.932391057274991,0.172726295799422,-0.087329537970072,-0.156114264651172,-0.542627889040196,0.039565988926476,-0.153028796529788,239.93]
#             ]
#     r.predict(test)
#     # X_train, X_test, y_train, y_test = train_test_split(data,data_class_outcomes,test_size=0.25, random_state=42)

#     # y_pred = implement_rfc(X_train,y_train,X_test)
#     # for x in y_pred:
#     #     print x
