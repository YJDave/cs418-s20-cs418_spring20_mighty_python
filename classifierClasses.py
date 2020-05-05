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
from sklearn.neighbors import KNeighborsClassifier

plt.rcParams['figure.figsize'] = [5, 5]

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
    plot_SVM_all_results(df_all_schools, learner, "SVM Learner for all Schools and the Majors")

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
    plot_SVM_results(df_major, learner, "SVM Learner grouped by Major")

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
    plot_SVM_results(df_school, learner, "SVM Learner grouped by School")

def KNNClassifyByAllSchools():
    df_school = pd.read_csv('data/school_classifier.csv')
    learner = KNeighborsClassifier()

    X , y = df_school[['Average Debt', 'Earnings']].values.tolist(), df_school['Good Investment']
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    dummy_clf = DummyClassifier()
    dummy_clf.fit(X_train, y_train)
    prediction = dummy_clf.predict(X_test)
    print("Baseline Classifier Accuracy:",metrics.accuracy_score(y_test, prediction))

    learner.fit(X_train, y_train)
    prediction = learner.predict(X_test)
    print("KNN Accuracy:",metrics.accuracy_score(y_test, prediction))
    
def plot_SVM_results(df, learner, text):

    df_plot=df.replace(False, 0)
    df_plot=df.replace(True, 1)
    X=df_plot.iloc[:,1:3]
    y=df_plot['Good Investment']
    #plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=y, s=50, cmap='autumn')
    #plt.scatter(learner.support_vectors_[:,0],learner.support_vectors_[:,1])
    
    ax = plt.gca()
    scatter = plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=y, s=50, cmap='cool')
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    xx = np.linspace(xlim[0], xlim[1], 30)
    yy = np.linspace(ylim[0], ylim[1], 30)
    YY, XX = np.meshgrid(yy, xx)
    xy = np.vstack([XX.ravel(), YY.ravel()]).T
    Z = learner.decision_function(xy).reshape(XX.shape)

    ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5,
               linestyles=['--', '-', '--'])

    ax.scatter(learner.support_vectors_[:, 0], learner.support_vectors_[:, 1], s=100,
               linewidth=1, facecolors='none', edgecolors='k')
    plt.title(text)
    plt.xlabel("Average Debts")
    plt.ylabel("Average Salaries")
    plt.legend(handles = scatter.legend_elements()[0], labels = ['False','True'] )
    plt.show()
    return

def plot_SVM_all_results(df, learner, text):

    df_plot=df.replace(False, 0)
    df_plot=df.replace(True, 1)
    X=df_plot.iloc[:,2:4]
    y=df_plot['Good Investment']
    #plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=y, s=50, cmap='autumn')
    #plt.scatter(learner.support_vectors_[:,0],learner.support_vectors_[:,1])
    
    ax = plt.gca()
    scatter = plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=y, s=50, cmap='cool')
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    xx = np.linspace(xlim[0], xlim[1], 30)
    yy = np.linspace(ylim[0], ylim[1], 30)
    YY, XX = np.meshgrid(yy, xx)
    xy = np.vstack([XX.ravel(), YY.ravel()]).T
    Z = learner.decision_function(xy).reshape(XX.shape)

    ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5,
               linestyles=['--', '-', '--'])

    ax.scatter(learner.support_vectors_[:, 0], learner.support_vectors_[:, 1], s=100,
               linewidth=1, facecolors='none', edgecolors='k')
    plt.title(text)
    plt.xlabel("Average Debts")
    plt.ylabel("Average Salaries")
    plt.legend(handles = scatter.legend_elements()[0], labels = ['False','True'] )
    plt.show()
    return