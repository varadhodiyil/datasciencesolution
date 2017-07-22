import os
import pickle
from sklearn.ensemble import RandomForestClassifier
import csv
import numpy
import datetime
from time import time
from sklearn import metrics
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# import pandas as pd
class CreditRiskAnalysis():
    def __init__(self):
        train_file = "train.csv"
        self.trainFile = os.path.join(BASE_DIR,train_file)
        self.testFile = "cs-test.csv"
        classified_dir = "classified"
        classified_dir = os.path.join(BASE_DIR,classified_dir)
        if not os.path.exists(classified_dir):
            os.makedirs(classified_dir)
        self.pickle_file = classified_dir + "/" + train_file+".pickle"
        self.classifier = None

    def readData(self,file):
        f = open(file, 'rb')
        data = list()
        try:
                reader = csv.reader(f)
                data = list(reader)
        finally:
                f.close()
        return data
    def getColumnIndex(self,column,needle):
        return column.index(needle)

    def update_Null(self , _list_, needle,default):
        updated = list()
        for l in _list_:
            if l == needle:
                l = default
            updated.append(l)
        return updated

    def clean_data(self):
        data = self.readData(self.trainFile)
        label_train ,train_data = data[0] , data[0:] 
        label_train = label_train[1:]
        train_data = list()
        for x in data:
            x = x[1:]
            train_data.append(x)
        train_data = train_data[1:]
        montly_income_index = self.getColumnIndex(label_train,"MonthlyIncome")
        dependend_index = self. getColumnIndex(label_train,"NumberOfDependents")
        monthly_income = list()
        depended = list()
        depended_temp = list()
        for x in train_data:
            try:
                value = float(x[montly_income_index ])
            except ValueError:
                value = 0
            monthly_income.append(value)
            try:
                value_d = int(x[dependend_index])
                depended.append(value_d)
            except ValueError:
                value_d = "NA"
            depended_temp.append(value_d)
        avg_monthly_income = float(sum(monthly_income) / len(monthly_income))
        average_depended = float(sum(depended))/float(len(depended))
        average_depended = round(average_depended,2)
        updated_monthly_income = self.update_Null(monthly_income,0,avg_monthly_income)
        updated_depended = self.update_Null(depended_temp,"NA",average_depended)
        avg_monthly_income = float(sum(updated_monthly_income) / len(train_data))
        new_train_data = list()
        index = 0
        for x in train_data:
            x[montly_income_index  ] = updated_monthly_income[index]
            x[dependend_index] = updated_depended[index]
            new_train_data.append(x)
            index = index + 1
        return label_train, new_train_data



    def benchmark(self,clf):
        print('_' * 80)
        print("Training: ")
        print(clf)
        t0 = time()
        clf.fit(self.X_train, self.y_train)
        train_time = time() - t0
        print("train time: %0.3fs" % train_time)

        t0 = time()
        pred = clf.predict(self.X_test)
        test_time = time() - t0
        print("test time:  %0.3fs" % test_time)

        score = metrics.accuracy_score(self.y_test, pred)
        print("accuracy:   %0.3f" % score)

        if hasattr(clf, 'coef_'):
            print("dimensionality: %d" % clf.coef_.shape[1])
            print("density: %f" % density(clf.coef_))

            if opts.print_top10 and feature_names is not None:
                print("top 10 keywords per class:")
                for i, label in enumerate(target_names):
                    top10 = np.argsort(clf.coef_[i])[-10:]
                    print(trim("%s: %s" % (label, " ".join(feature_names[top10]))))
            print()
        target_names =["0","1"]
        print("classification report:")
        print(metrics.classification_report(self.y_test, pred,
                                            target_names=target_names))

        print("confusion matrix:")
        print(metrics.confusion_matrix(self.y_test, pred))

        print()
        clf_descr = str(clf).split('(')[0]
        return clf_descr, score, train_time, test_time

    def loadModel(self):
        if os.path.exists(self.pickle_file):
            self.classifier = pickle.load(open(self.pickle_file,'rb'))
        else:
            print "unable to load Train file .. ! have you trained the model yet?"
            raise IOError , self.pickle_file

    def predict(self,dataset):
        result = dict()
        if self.classifier is None:
            self.loadModel()
        classes = self.classifier.classiferModel.classes_
        result['classes'] = classes
        result['predicted'] = self.classifier.classiferModel.predict(dataset)[0]
        result['probability'] = self.classifier.classiferModel.predict_proba(dataset)[0]
        return result

    def train(self):
        start = datetime.datetime.now()
        print "Started " , start
        label , dataset = self.clean_data()
        RANDOM_SEED=99
        clf = RandomForestClassifier(
            
            # max_depth=6,
            criterion='entropy',
            n_estimators=600,
            random_state=RANDOM_SEED )
        criterion_index = self.getColumnIndex(label,"SeriousDlqin2yrs")
        predited = list()
        samples = list()
        for x in dataset:
            predited.append(x[criterion_index])
            del x[criterion_index]
            samples.append(x)
        clf.fit(samples,predited)
        print clf.score(samples,predited)
        self.clf = clf
        self.classiferModel = clf
        self.__module__ = "resources"
        with open(self.pickle_file,"wb") as h :
            pickle.dump(self,h)
            h.close()
        end = datetime.datetime.now()
        print "ended" , end 
        print "Total Time " ,(end-start)
        
        # self.X_train = samples
        # self.y_train = predited
        # self.X_test = [dataset[1]]
        # self.y_test = ["0"]
        # self.benchmark(clf)

if __name__ == "__main__":
    c = CreditRiskAnalysis()
    c.train()
# data = [['0.766126609', '45', '2', '0.802982129', 9120.0, '13', '0', '6', '0', 2],['0.363636364','26','0','0.00999001',1000,'1','0','0','0','0']]

# c.predict(data)