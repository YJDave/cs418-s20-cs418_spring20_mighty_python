import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

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

from sklearn.dummy import DummyClassifier
features = ['ACTCMMID', 'TUITIONFEE_IN', 'D_PCTPELL_PCTFLOAN'] #'ACTCMMID', 'TUITIONFEE_IN', 'PCIP27', 'ADM_RATE', 'SAT_AVG'

X = combined_data[features]
y = combined_data['MD_EARN_WNE']
dummy_clf = DummyClassifier(strategy="most_frequent")
dummy_clf.fit(X, y)
print("Baseline Classifier Score: {0}".format(dummy_clf.score(X, y)))
