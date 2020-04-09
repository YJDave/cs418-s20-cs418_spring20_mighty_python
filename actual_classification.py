import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import metrics, svm
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
from sklearn import utils
from sklearn import linear_model
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier

pd.set_option('mode.chained_assignment', None)


college_data = pd.read_csv('CollegeScorecard_Raw_Data/MERGED2017_18_PP.csv', low_memory = False) # Opens our data into a dataframe


college_data['GRAD_DEBT_MDN10YR_SUPP'] = college_data['GRAD_DEBT_MDN10YR_SUPP'].replace(to_replace = 'PrivacySuppressed', value = np.nan) # Replace privacy suppressed with nan
college_data = college_data.dropna(subset=['GRAD_DEBT_MDN10YR_SUPP', 'ACTCMMID', 'C100_4_POOLED']) # Get rid of nan values if either in graduate debt median for 10 years, or cumulative act score
college_data['GRAD_DEBT_MDN10YR_SUPP']  = college_data["GRAD_DEBT_MDN10YR_SUPP"].astype(float)
college_data['GRAD_DEBT_MDN10YR_SUPP']  = college_data["GRAD_DEBT_MDN10YR_SUPP"].round(0)
# college_data['GRAD_DEBT_MDN10YR_SUPP'] = pd.to_numeric(college_data['GRAD_DEBT_MDN10YR_SUPP'], downcast='int')
used_data = college_data[['INSTNM','GRAD_DEBT_MDN10YR_SUPP', 'ACTCMMID']]


field_data = pd.read_csv('CollegeScorecard_Raw_Data/FieldOfStudyData1516_1617_PP.csv', low_memory = False)

field_data = field_data[['INSTNM', 'MD_EARN_WNE']]
result = field_data[field_data.MD_EARN_WNE != 'PrivacySuppressed']
result['MD_EARN_WNE'] = result['MD_EARN_WNE'].astype(int)
final = result.groupby('INSTNM').mean().astype(int).sort_values('MD_EARN_WNE')

combined_data = pd.merge(college_data, final, on='INSTNM')

features = ['ACTCMMID', 'TUITIONFEE_IN', 'D_PCTPELL_PCTFLOAN'] #'ACTCMMID', 'TUITIONFEE_IN', 'PCIP27', 'ADM_RATE', 'SAT_AVG'

X = combined_data[features]
y = combined_data['MD_EARN_WNE']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#Linear Regression
lm = linear_model.LinearRegression()
lm.fit(X_train, y_train)
model = lm.fit(X_train, y_train)
predictions = lm.predict(X_test)

plt.title("Linear Regression Predictions vs Actual")
plt.scatter(y_test, predictions)
plt.xlabel("Actual Values")
plt.ylabel("Predictions")
plt.show()

#SVM
svm = SVC()
svm.fit(X_train, y_train)

predictions = svm.predict(X_test)

# KNN
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
predictions = knn.predict(X_test)

plt.title("KNN Predictions vs Actual")
plt.scatter(y_test, predictions)
plt.xlabel("Actual Values")
plt.ylabel("Predictions")
plt.show()

# Adapted from https://towardsdatascience.com/solving-a-simple-classification-problem-with-python-fruits-lovers-edition-d20ab6b071d2
print('Accuracy of Logistic regression classifier on training set: {:.2f}'
     .format(lm.score(X_train, y_train)))
print('Accuracy of Logistic regression classifier on test set: {:.2f}'
     .format(lm.score(X_test, y_test)))

print('Accuracy of SVM classifier on training set: {:.2f}'
     .format(svm.score(X_train, y_train)))
print('Accuracy of SVM classifier on test set: {:.2f}'
     .format(svm.score(X_test, y_test)))

print('Accuracy of K-NN classifier on training set: {:.2f}'
     .format(knn.score(X_train, y_train)))
print('Accuracy of K-NN classifier on test set: {:.2f}'
     .format(knn.score(X_test, y_test)))
