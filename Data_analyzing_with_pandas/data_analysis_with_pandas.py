# -*- coding: utf-8 -*-
"""Data_analysis_with_pandas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pKLwu69lJ8iBjjd5YhG2OWTrb8wJ_255
"""

import pandas as pd
# .read_csv(): use for read data in pandas.
covid_data=pd.read_csv("covid19.csv")
#print(covid_data.head(100)) # Head use for view data from top to table by default it show 5 rows
print(covid_data)
print(covid_data.info()) # info(): use for view some basic information of data
print(covid_data.describe()) #describe(): use for view some statistical information like mean,median,std,max,min..etc
print(covid_data.columns) #columns: property contains the list of columns within the data frame
print(covid_data.shape) # shape: property show the rows and column
print(type(covid_data))
# Pandas format is similar to below this.
# covid_data_dict={
#     'date':['8/30/2020','8/31/2020','9/2/2020'],
#     'new_cases':[1444,1365,975],
#     'new_deaths':[1,4,8],
#     'new_tests':[53541.0,42583.0,None]
# }
# Pandas format is not similar to below this
# covid_data_list=[
#     {'date':'8/30/2020','new_cases':1444,'new_deaths':1,'new_tests':53541.0},
#     {'date':'8/31/2020','new_cases':1365,'new_deaths':4,'new_tests':42583.0},
#     {'date':'9/2/2020','new_cases':975,'new_deaths':8,'new_tests':None}
# ]
print(covid_data['date'])
print(covid_data['new_cases'][245])
# Pandas also provides the .at method to directly retrive at a specific row and column
print(covid_data.at[240,'new_cases'])
print(covid_data.at[246,'new_deaths'])
# same as covid_data['new_cases'] to covid_data.new_cases
print(covid_data.new_cases)
# List of columns within the indexing notation [] to access a subset of the data frame
covid=covid_data[['date','new_cases']]
# Sometimes you might need a full copy of data frame, in which cases you can use the .copy() nmethod
covid_data_copy=covid_data.copy()
print(covid_data_copy)
# To access a specific row of data pandas provides the .loc methods.
print(covid_data.loc[225])
# Fetching dataset using .iloc , use slicing
print(covid_data_copy.iloc[2:10,1:])
# each row and column retrieved is also a series object
# for first or last few rows of data we can use .head and .tail methods.
print(covid_data.head(4))
print(covid_data.tail(3))
print(covid_data.at[0,'new_cases'])
print(type(covid_data.at[0,'new_cases']))
print(covid_data.head(10))
# We can find the first index that doesn't contain a NaN value using .first_valid_index() method of a series.
print(covid_data.new_tests.first_valid_index())
print(covid_data.loc[109:113])
# .sample method can be used to retrieve a random sample pf rows from the data frame
print(covid_data.sample(10))
# Analyzing data from data frames
# 1) What is the total number of reported cases and deaths related to covid19 ?
total_cases=covid_data.new_cases.sum()
total_deaths=covid_data.new_deaths.sum()
print("The number of reported cases {} and number of reported deaths {}".format(total_cases,total_deaths))
# 2) What is the overall death rate (ratio of reported deaths to reported cases) ?
death_rate=total_deaths/total_cases
print("The overall reported deaths rate in Itly is {:.2f} %".format(death_rate*100))
# 3) What is the overall number of test conducted? A total of 935310 tests were conducted before daily test numbers were being reported.
# we can check the first non-Nan index using first_valid_index
initial_test=935310
total_tests=initial_test+covid_data.new_tests.sum()
print("Total covid test is {:.2f}".format(total_tests))
# 4) What fraction of test returned a positive result ?
positive_rate=total_cases/total_tests
print("{:.2f}% of tests in Itly led to a positive diagnosis.".format(positive_rate*100))
# 5) The days which had more than 1000 reported cases ?
high_new_cases=covid_data.new_cases > 1000
print(high_new_cases) # Return a series containing True and False boolean values.
print(covid_data[high_new_cases])
# in singal line make above case
high_cases=covid_data[covid_data.new_cases > 1000]
print(high_cases)
# To view all the rows, we can modify some display options.
from IPython.display import display
with pd.option_context('display.max_row',100):
    display(covid_data[covid_data.new_cases > 1000])
# Try to determine the days when the ratio of cases reported to tests cunducted is higher than the overall positive rate
print(positive_rate)
positive_rate_data=covid_data[covid_data.new_cases/covid_data.new_tests>positive_rate]
print(positive_rate_data)
#
positive_data=covid_data.new_cases/covid_data.new_tests
print(positive_data)
covid_data['positive_data']=covid_data.new_cases/covid_data.new_tests
print(covid_data)
print(covid_data[positive_data>positive_rate])
# For remove the column using the .drop method
#
covid_data.drop(columns=['positive_data'],inplace=True)
#covid_data1=covid_data.drop(['positive_data'],axis=1)
print(covid_data)
# The row can also be sorted by a specific column using .sort_values
print(covid_data.sort_values('new_cases',ascending=False).head(10))
print(covid_data.sort_values('new_deaths', ascending=False).head(10))
#print(covid_data.sort_values('new_cases').head(10)) # By default ascending is True
print(covid_data.sort_values('new_cases').head(10))
'''seem like the count of new cases on june 20th was -148, a negative number, not somthing we might have expected
but that's the real world data.It could simply be data entery error, or may some other..
 Let's look at the some of days before and after june 2oth
'''
print(covid_data.loc[169:175])
''' If this was indeed a data entry error we can use one of the following approaches for dealing with missing value
1. Replace it with 0
2. Replace it with the average of the entire column
3. Replace it with the average of the values on the previous and next date
4. Discard toe row entirely'''
# We can pick apporach 3.
covid_data.at[172,'new_cases']=(covid_data.at[171,'new_cases']+covid_data.at[173,'new_cases'])/2
print(covid_data.loc[171:175])

# Working with dates
print(covid_data.date)
''' The data type date is currently object, so pandas does not know that this column is a date.
we convert it into a date time column using the pd.to_datetime method'''
covid_data['date']=pd.to_datetime(covid_data.date)
print(covid_data['date'])
''' We can now extract different parts of the data into seprated colomns using the DatetimeIndex class'''
covid_data['year']=pd.DatetimeIndex(covid_data.date).year
covid_data['month']=pd.DatetimeIndex(covid_data.date).month
covid_data['day']=pd.DatetimeIndex(covid_data.date).day
covid_data['weekday']=pd.DatetimeIndex(covid_data.date).weekday
print(covid_data)
# Query the rows for may
covid_data_may=covid_data[covid_data.month==5]
print(covid_data_may)
covid_data_may_matrix=covid_data_may[['new_cases','new_deaths','new_tests']]
print(covid_data_may_matrix)
covid_data_may_total=covid_data_may_matrix.sum()
print(covid_data_may_total)
# Operations above can also be combined into a single statement.
print(covid_data[covid_data_may==5][['new_cases','new_deaths','new_tests']].sum())
# We might want to aggregate using the .mean method
# Overall average
print(covid_data.new_cases.mean().round(2))
# Average of sunday..
print(covid_data[covid_data.weekday==6].new_cases.mean().round(2))

# Grouping and aggregation..
''' We might be want to summarize the daywise data and create a new dataframe with month-wise data.
 This is where the groupby finction useful.
 '''
covid_month_wise=covid_data.groupby('month')[['new_cases','new_deaths','new_tests']].sum()
print(covid_month_wise)
print(covid_month_wise.loc[5])
covid_weekday_wise=covid_data.groupby('weekday')[['new_cases','new_deaths','new_tests']].mean()
print(covid_weekday_wise)
print(covid_data)
'''Apart from grouping, another form of aggregration is to calculate the running or cumulative sum of cases
test or death up to current date for each row useing cumsum'''
covid_data['total_cases']=covid_data.new_cases.cumsum()
covid_data['total_deaths']=covid_data.new_deaths.cumsum()
covid_data['total_tests']=covid_data.new_tests.cumsum()
print(covid_data)
# Mearging data from multiple sources
'''To determine other metrics like test per million, cases etc.'''
country_data=pd.read_csv("country_data.csv")
print(country_data)
itly=country_data[country_data.location=='Italy']
print(itly)
# We can merge this data into our existing data frame by adding more columns.We need at least one common column
covid_data['location']='Italy'
print(covid_data)
# We can now add  the columns from county_data to covid_data using the .merge method.
merge_data=pd.merge(covid_data,country_data,on='location')
print(merge_data)
print(merge_data.shape)
# We can now calculate metrics like cases per million, deaths per million and test per million
merge_data['cases_per_million']=merge_data.total_cases*1e6/merge_data.population
merge_data['deaths_per_million']=merge_data.total_deaths*1e6/merge_data.population
merge_data['test_per_million']=merge_data.total_tests*1e6/merge_data.population
print(merge_data)
# Writing data back to files
'''After doing some analysis and adding new columns to data frame. Itwould be good idea to write the result back to file'''
result_data=merge_data[[
    'date','new_cases','total_cases','new_deaths','total_deaths','new_tests','total_tests','cases_per_million',
    'deaths_per_million','test_per_million'
]]
print(result_data)
result_data.to_csv('result.csv',index=None)

#plot grahp for new cases
print(result_data.new_cases.plot())

'''While this plot shows the overall trend, it's hard to tell where the peak occured, as there are no dates on x -axis.
We can use the the date column as the index for the the data frame to address this issue, set_index method'''
result_data.set_index('date',inplace=True)
print(result_data)

# Let's plot the new cases and new deaths per day as line graphs.
result_data.new_cases.plot()
result_data.new_deaths.plot()

# We compare the total cases vs total deaths.
result_data.total_cases.plot()
result_data.total_deaths.plot()

# Let's see how the death rate and positive testing rates vary over time
death_rate=result_data.total_deaths/result_data.total_cases
death_rate.plot(title="Death Rate")

positive_rate=result_data.total_cases/result_data.total_tests
positive_rate.plot(title="Positive Rate")

# Plotsome month-wise data using bar chart to visualize the trend at a higher level
covid_month_wise.new_cases.plot(kind='bar')

covid_month_wise.new_tests.plot(kind='bar')