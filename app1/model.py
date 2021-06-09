from . import *
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics


class MlModel:

    def __init__(self):

        self.df = pd.read_csv("app1/dataset.csv")
        X = self.df.iloc[:, :-1].values
        y = self.df.iloc[:, 3].values

        labelEncoder_gender = LabelEncoder()
        X[:, 0] = labelEncoder_gender.fit_transform(X[:, 0])

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.25, random_state=0)
        self.sc_X = StandardScaler()

        X_train = self.sc_X.fit_transform(X_train)
        X_test = self.sc_X.transform(X_test)

        self.KNNclassifier = KNeighborsClassifier(
            n_neighbors=5, metric="minkowski", p=2)
        self.KNNclassifier.fit(X_train, y_train)

        self.NBclassifier = GaussianNB()

        self.NBclassifier.fit(X_train, y_train)

        KNNy_pred = self.KNNclassifier.predict(X_test)
        NBy_pred = self.NBclassifier.predict(X_test)

        self.KNNaccuracy = metrics.accuracy_score(y_test, KNNy_pred)
        self.NBaccuracy = metrics.accuracy_score(y_test, NBy_pred)

    def getAccuracy(self):
      return {
        'knnAccuracy': str(self.KNNaccuracy*100), 'nbAccuracy': str(self.NBaccuracy*100)
      }
    def predict(self, test_data):
        print(test_data)
        test_predict = [test_data]
        test_predict = self.sc_X.transform(test_predict)
        print(test_predict)
        result = self.KNNclassifier.predict(test_predict)
        print(result)
        result1 = self.NBclassifier.predict(test_predict)
        print(result1)
        return {
            "knn": result[0], "nb": result1[0] 
        }
