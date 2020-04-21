field_data = pd.read_csv('CollegeScorecard_Raw_Data/FieldOfStudyData1516_1617_PP.csv', low_memory = False)
field_data = field_data[['INSTNM', 'MD_EARN_WNE','CIPDESC']]
result = field_data[field_data.MD_EARN_WNE != 'PrivacySuppressed']
result['MD_EARN_WNE'] = result['MD_EARN_WNE'].astype(int)
result = result.groupby(['CIPDESC', 'INSTNM']).mean().astype(int).sort_values('CIPDESC')
result