# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

# file = pd.read_csv('iris.csv')

# print(file)


# ####Absolute path:
# ##C:\Users\AneleMahlangu\css_2024day2\data_02

# ####Relative path:
# ####iris.csv or data_02/iris.csv 

# #you can get data online

# df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

# print(df)

# ##OR

# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# file = pd.read_csv(url)

# print(file)
# # the data does not have column names

# column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

# df = pd.read_csv(url,header=None, names= column_names)

# print(df)

# file = pd.read_csv("data_02/Geospatial Data.txt",sep = ";") #use a "separare" for text files

# print(file)

# ##file2 = pd.read_excel("data_02/residentdoctors.xlsx",sheet= "sheet1")


df = pd.read_excel("data_02/residentdoctors.xlsx")
print(df)

#to change or add a column in an excel file
print(df.info())

df["LOWER_AGE"] = df["AGEDIST"].str.extract('(\d+)-') #"d" is a o to 9 digits#CREATE A NEW COLUMn which is a string
print(df.info())
df["LOWER_AGE"] = df["AGEDIST"].astype(int)#covert this to an intiger from object
df["UPPER_AGE"] = df["AGEDIST"].str.extract('(\d+)-')
print(df.info())


file3 = pd.read_json("data_02/student_data.json")
print(file3)

url = "https://raw.githubusercontent.com/Asabele240701/css4_day02/main/effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv"

#df = dataframe
df = pd.read_csv(url)
print(df.info())
print(df.describe)

# df = pd.read_csv("data_02/person_work.csv", names = ["data_time","x","y","z"])

"""
Transformation
"""

df = pd.read_csv("data_02/country_data_index.csv")
df = pd.read_csv("data_02/country_data_index.csv",index_col=0) #To avoid the appearance of the "Unnamed: 0" column, you can either specify the existing index column from your CSV file when reading the data, or you can use the index_col parameter to explicitly specify which column you want to use as the index.


"""
WORKING WITH DATES
30-05-2024 (UK)
01-30-2024(US)
"""
#To make dates be in the same format

import pandas as pd
df = pd.read_csv("data_02/time_series_data.csv",index_col=0) #to remove the forst column
print(df)
print(df.info())

#TO CONVERT THE COLUMN TO DATE TIME COLUMN
df['Date'] = pd.to_datetime(df['Date'])
print(df.info())

#TO SPECIFY FORMAT
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y') #FIRST YOU ACCESS, CONVERT TO DAYTIME
print(df.info())

#ORRRRR
# Split the 'Date' column into separate columns for year, month, and day
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
print(df.info())


"""
.extract
.astype
.str
"""

"""
Nans and wrong formats
date formats, outliers
"""
df = pd.read_csv('data_02/patient_data_dates.csv')
df = pd.read_csv('data_02/patient_data_dates.csv',index_col=0) #remove extra first column
df.drop(index=26,inplace=True) #to remove the nan in index 26
df['Date'] = pd.to_datetime(df['Date'])  #convert the date
print(df.info())

# Allows you to see all rows
pd.set_option('display.max_rows',None)
print(df)

#2 nans in calories
avg_cal = df["Calories"].mean()

df["Calories"].fillna(avg_cal, inplace = True) #fills a nan/blank value with average calculation


"""
Best practices
dropping nas/removing
"""

#removing nans
df.dropna(inplace = True)
df = df.reset_index(drop=True) #as you remove, you need to reset the index as it gets messed up

#to replace or remove rows
df.loc[7, 'Duration'] = 45 #change the value in index 7, colomn duration
##ORRR
df.drop(7, inplace = True) #remove the row
##oR 
df['Duration'] = df['Duration'].replace([450],45)


#Removing Duplicates – Using drop_duplicates()
df.drop_duplicates(inplace = True)


"""A more cleaner code"""

import pandas as pd

df = pd.read_csv('data_02/patient_data_dates.csv')

pd.set_option('display.max_rows',None)

print(df)

# Drop Index Column:

df.drop(['Index'],inplace=True,axis=1)

print(df)

# Fill NaNs or empty fields in Calorie Column

x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)

print(df)

# Convert Wrong Date Format in Date Column

df['Date'] = pd.to_datetime(df['Date'])

# Drop NaT field in Date Column

df.dropna(subset=['Date'], inplace = True)

print(df)

# Remove any rows that have NaNs or empty fields
# Here only the row 1 for the MaxPulse column as the rest have been resolved
df.dropna(inplace = True)

# Reset index
df = df.reset_index(drop=True)

print(df)

# Remove duplicates found in line 10 and 11
df.drop_duplicates(inplace = True)

df = df.reset_index(drop=True)

print(df)
##################################################################

"""
Applying Data Transformations
"""
import pandas as pd

df = pd.read_csv('data_02/iris.csv')
print(df)
print(df.columns)

col_names = df.columns.tolist()
print(col_names)

"""
add a column with a name "sepal_length_sq""
"""

df["sepal_length_sq"] = df["sepal_length"]**2
grouped = df.groupby("class")
mean_squared_values = grouped['sepal_length_sq'].mean()
print(mean_squared_values)

##################################################
"""Working with multiple files
"""
import pandas as pd

# Read the CSV files into dataframes
df1 = pd.read_csv('data_02/person_split1.csv')
df2 = pd.read_csv('data_02/person_split2.csv')

# Concatenate the dataframes or add 2 dataframes together
df = pd.concat([df1, df2], ignore_index=True)


##########################
"""merging files together
An inner join returns only the rows where there is a match in both dataframes on the specified "on" column (in this case, the "id" column). If there is no match, the row is excluded from the result.
An outer join returns all the rows from both dataframes. If there is no match for a row in either dataframe, the missing values will be filled with NaNs. Left and Right Joins are possible too.
"""

df1 = pd.read_csv('data_02/person_education.csv')
df2 = pd.read_csv('data_02/person_work.csv')

## inner join,(they are related by the "id" column)
df_merge = pd.merge(df1,df2,on='id') #specifying the relationship between thne 2 files is the"id"
print(df_merge)


df_merge = pd.merge(df1, df2, on='id', how='outer')#returns all the rows from both dataframes
##inner join = both, outer join = all, left join = all first, right join= all last
################################################

"""
Filtering data
"""
df["class"] = df["class"].str.replace("Iris-","")
df = df[df['sepal_length''] >5]
df = df[df["class"] == "virgica] 
        
# Filtering data
df = pd.read_csv('data_02/person_education.csv')

# Filter data for females (class == 'Iris-versicolor')
iris_versicolor = df[df['class'] == 'Iris-versicolor']

# Calculate the average iris_versicolor_sep_length
avg_iris_versicolor_sep_length = iris_versicolor['sepal_length'].mean()

df['class'] = df['class'].str.replace('Iris-', '')

############################
"""Loading data
"""

#our cleaned files to text files/csv
# df.to_csv("data_02/output/iris_data_cleaned.csv")
# df.to_csv("data_02/output/iris_data_cleaned.csv", index=False) #specifying If you don't want the Pandas index column
df.to_csv('cleaned_outputday2.csv') ####to export the cleaned data








