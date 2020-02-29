
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('NCES_Enrollment_Data.csv', dtype={'Year':np.str, 'Total Enrollment':np.int32, 'Elementary & Secondary enrollment':np.int32,
       'Public elementary and secondary':np.int32,
       'Private elementary and secondary schools':np.int32,
       'Degree-granting postsecondary institutions Total':np.int32,
       'Public post graduation colleges':np.int32, 'Private post graduation colleges':np.int32}, thousands=',')


data.plot.line(x="Year", y="Total Enrollment", title="Enrollment trend in U.S.", legend=False)

data.plot(x="Year", y="Total Enrollment", title="Enrollment trend in U.S.", legend=False, style='-o',
    colormap='jet', xticks=data['Year'].index, rot=50)

# sns.barplot(y="Year", x="Total Enrollment", data=data)
