
# cs418-s20-cs418_spring20_mighty_python

## Files description
#### ```data/```

Contains the data used in the project

#### ```sean-eda.ipynb```

This file contains code/implementation for...

1. Data cleaning of CollegeSchool Board data for interactive visualization. This notebook loads the data from [CollegeBoard](https://collegescorecard.ed.gov/data/) and clean file `MERGED2017_18_PP.csv` (all U.S. university wise data of year 2017-2018) and `FieldOfStudyData1516_1617_PP.csv` (Field wise salary, debt etc. data). The cleaned data is stored as `cleaned_college_data.csv` and `cleaned_salary_data.csv` under `data/` directory. Both file data are further merged and mapped to `best_value_data.csv` for data visualization and ML model.

2.  (i) An average earnings 1 year out of college and (ii) Median college debt after graduating college visualizations of the 2017-2018 data

3. Tried different ML model to classify the 2017-2018 year college data into Best value or not. i.e. `KNeighborsClassifier, MLPClassifier`

#### ```main.ipynb```

This file contains code/implementation for...

1. Data visualization about different trends i.e. student enrollment growth, student debt growth, graduation expenses, student loan distributions, current post secondary enrollment distributions etc. All the data used in the file is stored inside `data/` directory, for which description is given below. The preprocessing for this data is either done manual if very minor of done in this script. Different visualizations with their data source, takeaways and description is included in file.

2. Machine Learning model for predicting the trends of enrollment at UIC. Although, this does not directly address our project definition questions, we could not find better Machine Learning definition which can be done on the data we had. We make use of the `CollegeScoreBoard` data, all university data over the year of 1997-2019. We extract the UIC data from all files(`MERGED1996_97_PP, MERGED1998_99_PP, ... to MERGED2018_19_PP`) and stored in `data/UIC_enrollment_data.csv` file. The data is pre-processed to only required column values. We tried two `sklearn-LinearRegression` and `Tensorflow-Sequential` model with 12 hidden neurons and `softmax` activation function. All model performance, implementation, data training is included in notebook.

NOTE: When you run, the code load csv data from `MERGED*_*_PP.csv` file is commented. Because, the files are not included in repository as it is very large dataset. If you want to run the script to load data from all csvs then you need to first download the data from [CollegeBoard](https://collegescorecard.ed.gov/data/) and provide the path to download files in script.

#### ```SVM_learner.csv```

This file contains code/implementation for...

1. Machine Learning model for classification of schools, majors and major at school into Best value or not. The model is trained on preprocessed data `best_value_data.csv` from [CollegeBoard](https://collegescorecard.ed.gov/data/) of year 2017-2018. The further data cleaning and manipulation for the model is included in notebook. The results of the SVM model using `sklearn` is also included in notebook.

All other files are indirectly used in above files or for project/presentation submission.


## How to use our interactive data visualization
1. [Student Debt and Earnings Sort](https://datastudio.google.com/open/1g6G-O8LygSsjNdDV32BJNbLDH6IjJqIA)
To use click on the link, which then allows you to sort the data by state, instituion name, degree name, debt, and earnings. See Final Report for analysis.

2. ["Best Value" Schools](https://datastudio.google.com/u/0/reporting/1UYDnVQdFf6_hKf1z2TgFMWtHsNvXl8s6/page/5WZNB)
To use click on the link, which then allows you to sort the data by state and major. This shows the earnings divded by debt. See Final Report for analysis.


Note: Other non-interactive visualizations can be run from file `main.ipynb`

## Data

1. In the data directory you see our cleaned data, the main files include ```best_value_data.csv```, ```major_classifier.csv```, ```school_classifier.csv```, and ```all_school_classifier.csv```

2. ```best_value_data.csv``` contains our cleaned dataset with the best value column calcuated from earnings divided by debt

3. ```major_classifier.csv```, ```school_classifier.csv```, and ```all_school_classifier.csv``` contains the dataframe as a CSV from the data prepared for the classifier functions. This makes it easy to pass through to our classifier class.

4. ```2018_fees.csv, 2019_Graduates.csv, inflation_rate.csv, NCES_Enrollment_Data.csv, NCES_graduate_fees.csv, NCES_student_loan.csv, non_mortage_loans.csv, student_loan_by_age.csv, student_loan_by_amount.csv``` are data for visualizations present in `main.ipynb` file. The source of the data is [National Center for Educational Statistics](https://nces.ed.gov/datalab/index.aspx) and [Board of Governors of Federal Reserve System](https://www.federalreserve.gov/releases/g19/current/default.htm). Both of the sources allows to create dynamic tables of values according to the requirement. Suppose selecting the Number of Student enrollment over Years seperated by Private/Public schools, age, race etc. Therefore, we don't need to download large dataset. 

5. ```UIC_enrollment_data.csv``` is extracted from (`MERGED1996_97_PP, MERGED1998_99_PP, ... to MERGED2018_19_PP`) of [CollegeBoard](https://collegescorecard.ed.gov/data/) dataset, which is used for Linear Regression Machine Learning model.


## References
Mostly research blogs, report and articles related to student education treds


1. U.S. Department of Education releases the data [link](https://www.ed.gov/news/press-releases/secretary-devos-delivers-promise-provide-students-relevant-actionable-information-needed-make-personalized-education-decisions)

2. Trends in Higher Education Series of research reports by CollegeBoard [link](https://research.collegeboard.org/trends/trends-higher-education)

3. Trends in Student Loan Debt for Graduate School Completers by NCES [link](https://nces.ed.gov/programs/coe/pdf/coe_tub.pdf)

4. Payback Time? Measuring Progress on Student Debt Repayment by New York Fed [link](https://libertystreeteconomics.newyorkfed.org/2015/02/payback_time_measuring_progress_on_student_debt_repayment.html)

5. A Look at the Shocking Student Loan Debt Statistics for 2020 by Student Loan Hero [link](https://studentloanhero.com/student-loan-debt-statistics/)*

6. What do we know about our nation’s students and schools? by NCES [link](https://nces.ed.gov/fastfacts/display.asp?id=372)

7. College Graduation Statistics by EducationData [link](https://educationdata.org/number-of-college-graduates/)

8. Trends in Graduate Student Loan Debt by NCES [link](https://nces.ed.gov/blogs/nces/post/trends-in-graduate-student-loan-debt)

9. QUARTERLY REPORT ON HOUSEHOLD DEBT AND CREDIT[link](https://www.newyorkfed.org/medialibrary/interactives/householdcredit/data/pdf/hhdc_2019q3.pdf)*

10. Just Released: Press Briefing on Student Loan Borrowing and Repayment Trends, 2015 by New York Fed [link](https://libertystreeteconomics.newyorkfed.org/2015/04/just-released-press-briefing-on-student-loan-borrowing-and-repayment-trends-2015.html)*

11. How many educational institutions exist in the United States? by NCES [link](https://nces.ed.gov/fastfacts/display.asp?id=84)

## Dataset

1. NCES DataLab, National Center for Educational Statistics [link](https://nces.ed.gov/datalab/index.aspx)*

2. College Scorecard dataset, data on student completion, debt and repayment, earnings, and more by U.S. Department of Education[link](https://collegescorecard.ed.gov/data/)*

3. Enrollment in elementary, secondary, and degree-granting postsecondary institutions by NCES 1869-70 through fall 2028 [link](https://nces.ed.gov/programs/digest/d18/tables/dt18_105.30.asp)*

4. Inflation rate in United States by US INFLATION CALCULATOR [link](https://www.usinflationcalculator.com/inflation/historical-inflation-rates/)*

5. Average graduate tuition and required fees in degree-granting postsecondary institutions, by control of institution and percentile of charges: 1989-90 through 2016-17 [link](https://nces.ed.gov/programs/digest/d17/tables/dt17_330.50.asp)*

6. Percentage of graduate degree completers with student loan debt and average cumulative amount owed, by level of education funded and graduate degree type, institution control, and degree program: Selected years, 1999-2000 through 2015-16 by NCES [link](https://nces.ed.gov/programs/digest/d17/tables/dt17_332.45.asp)*

7. Average undergraduate tuition and fees and room and board rates charged for full-time students in degree-granting postsecondary institutions, by level and control of institution: Selected years, 1963-64 through 2017-18 [link](https://nces.ed.gov/programs/digest/d18/tables/dt18_330.10.asp)*

8. Different loan statistics by Board of Governors of Federal Reserve System [link](https://www.federalreserve.gov/releases/g19/current/default.htm)*
