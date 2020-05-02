import pandas as pd
import numpy as np
dtype=np.float64
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
import string
import re
from IPython.display import display, Latex, Markdown
from sklearn.dummy import DummyClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import sklearn.metrics as metrics
from sklearn.dummy import DummyClassifier
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def ClassifyByAllSchools():

    df_all_schools = pd.read_csv('data/all_school_classifier.csv')
    #learner for all schools and majors
    learner = SVC(kernel = 'linear',gamma='auto')

    X , y = df_all_schools[['DEBTMEAN', 'MD_EARN_WNE']].values.tolist(), df_all_schools['Good Investment']
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    dummy_clf = DummyClassifier()
    dummy_clf.fit(X_train, y_train)
    prediction = dummy_clf.predict(X_test)
    print("Baseline Classifier Accuracy:",metrics.accuracy_score(y_test, prediction))

    learner.fit(X_train, y_train)
    prediction = learner.predict(X_test)
    print("SVM Accuracy:",metrics.accuracy_score(y_test, prediction))

def ClassifyByMajor():

    df_major = pd.read_csv('data/major_classifier.csv')
    # learner for major
    learner = SVC(kernel = 'linear',gamma='auto')

    X , y = df_major[['Average Debt', 'Earnings']].values.tolist(), df_major['Good Investment']
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    dummy_clf = DummyClassifier()
    dummy_clf.fit(X_train, y_train)
    prediction = dummy_clf.predict(X_test)
    print("Baseline Classifier Accuracy:",metrics.accuracy_score(y_test, prediction))


    learner.fit(X_train, y_train)
    prediction = learner.predict(X_test)
    print("SVM Accuracy:",metrics.accuracy_score(y_test, prediction))

def ClassifyBySchool():

    df_school = pd.read_csv('data/school_classifier.csv')
    learner = SVC(kernel = 'linear',gamma='auto')

    X , y = df_school[['Average Debt', 'Earnings']].values.tolist(), df_school['Good Investment']
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    dummy_clf = DummyClassifier()
    dummy_clf.fit(X_train, y_train)
    prediction = dummy_clf.predict(X_test)
    print("Baseline Classifier Accuracy:",metrics.accuracy_score(y_test, prediction))

    learner.fit(X_train, y_train)
    prediction = learner.predict(X_test)
    print("SVM Accuracy:",metrics.accuracy_score(y_test, prediction))
