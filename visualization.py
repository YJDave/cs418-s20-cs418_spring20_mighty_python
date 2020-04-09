import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('mode.chained_assignment', None)

college_data = pd.read_csv('CollegeScorecard_Raw_Data/MERGED2017_18_PP.csv', low_memory = False) # Opens our data into a dataframe


college_data['GRAD_DEBT_MDN10YR_SUPP'] = college_data['GRAD_DEBT_MDN10YR_SUPP'].replace(to_replace = 'PrivacySuppressed', value = np.nan) # Replace privacy suppressed with nan
college_data = college_data.dropna(subset=['GRAD_DEBT_MDN10YR_SUPP', 'ACTCMMID', 'C100_4_POOLED']) # Get rid of nan values if either in graduate debt median for 10 years, or cumulative act score
print("Mean median ACT Score: ", college_data['ACTCMMID'].mean())
print("Max median ACT Score: ", college_data['ACTCMMID'].max())
print("Min median ACT Score: ", college_data['ACTCMMID'].min())
college_data['GRAD_DEBT_MDN10YR_SUPP']  = college_data["GRAD_DEBT_MDN10YR_SUPP"].astype(float)
college_data['GRAD_DEBT_MDN10YR_SUPP']  = college_data["GRAD_DEBT_MDN10YR_SUPP"].round(0)
# college_data['GRAD_DEBT_MDN10YR_SUPP'] = pd.to_numeric(college_data['GRAD_DEBT_MDN10YR_SUPP'], downcast='int')
college_data['GRAD_DEBT_MDN10YR_SUPP'].unique()
used_data = college_data[['INSTNM','GRAD_DEBT_MDN10YR_SUPP', 'ACTCMMID']]

# ACT Score
sns.distplot(used_data['ACTCMMID'])
plt.title("Average ACT Score")
plt.xlabel("ACT Score")
plt.ylabel("Probability")

sns.distplot(used_data['GRAD_DEBT_MDN10YR_SUPP'])
plt.title("Average debt repayment is around $275 a month over 10 years")
plt.xlabel("Repayment amount per month")
plt.ylabel("Probability")

sns.scatterplot(x="GRAD_DEBT_MDN10YR_SUPP", y="ACTCMMID", data=used_data)
plt.xticks(np.arange(0, used_data['GRAD_DEBT_MDN10YR_SUPP'].max()+50, 50.0))
plt.title("Average monthly payment for a 10 year debt repayment plan compared to ACT averages per school")
plt.xlabel("Repayment amount in USD")
plt.ylabel("ACT Score")
plt.show()

field_data = pd.read_csv('CollegeScorecard_Raw_Data/FieldOfStudyData1516_1617_PP.csv', low_memory = False)

field_data = field_data[['INSTNM', 'MD_EARN_WNE']]
result = field_data[field_data.MD_EARN_WNE != 'PrivacySuppressed']
result['MD_EARN_WNE'] = result['MD_EARN_WNE'].astype(int)
final = result.groupby('INSTNM').mean().astype(int).sort_values('MD_EARN_WNE')
sns.distplot(final)
plt.title("Median Salary per College")
plt.xlabel("Salary in USD")
plt.ylabel("Proability")
plt.show()
print("Max salary: ", final.max())
print("Min salary: ", final.min())
print("Median salary: ", final.median())

combined_data = pd.merge(college_data, final, on='INSTNM')
