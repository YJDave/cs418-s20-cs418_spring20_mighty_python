
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Load data from CSV downloaded from NCES(https://nces.ed.gov/programs/digest/d18/tables/dt18_105.30.asp)
data = pd.read_csv('NCES_Enrollment_Data.csv', dtype={'Year':np.str, 'Total Enrollment':np.int32, 'Elementary & Secondary enrollment':np.int32,
       'Public elementary and secondary':np.int32,
       'Private elementary and secondary schools':np.int32,
       'Degree-granting postsecondary institutions Total':np.int32,
       'Public post graduation colleges':np.int32, 'Private post graduation colleges':np.int32}, thousands=',')


"""
    Clean 'Year' column as following for example

    1869-70 => 1869
    Fall 1959 => 1959

    And conver year column in integer
"""

data['Year'] = data['Year'].replace(regex=r'(Fall )()', value='')
data['Year'] = data['Year'].replace(regex=r'()(-)(\d{2})*', value='')
data['Year'] = pd.to_numeric(data['Year'])

# data.plot.line(x="Year", y="Total Enrollment", title="Enrollment trend in U.S.", legend=False)

# data.plot(x="Year", y="Total Enrollment", title="Enrollment trend in U.S.", legend=False, style='-o',
#     colormap='jet', xticks=data['Year'].index, rot=50)

# plt.show()
# sns.barplot(y="Year", x="Total Enrollment", data=data)

# Show total enrollment data from 1990-2016
fig, ax = plt.subplots()
plt.plot(data['Year'][12:].values, data['Total Enrollment'][12:].values, '-r')
plt.xlabel("Year")
plt.ylabel("Total Enrollment")
plt.title("Enrollment trend in U.S.")
plt.show()

