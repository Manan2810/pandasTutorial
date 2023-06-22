import pandas as pd
df=pd.read_csv('/Users/mananmehra/Desktop/reportcard.csv')
print(df)
# ! print the dates when it rained
print(df['dates'][df['event']=='Rain'])
# ! to know how many rows and columns are there we use the shape method
rows,column=df.shape
print("Rows=",rows)
print("Columns=",column)
# !to print the initial few rows we can do the head() function
print(df.head(3))# it will print the first 3 rows of the table
# !to print the last few rows we can do the tail() function
print(df.tail(3))# it will print the lastt 3 rows of the table
# !to print the all the column names of table
print(df.columns)
# !to print the value of all the column respectively -> (df.column_name)
print(df.dates)
# !to print the value of multiple columns respectively 
print(df[['dates','event','temperature']])

# !to print the maximum value of the column
print('maximum temperture is',df['temperature'].max())
# !to print the minimum value of the column
print('minimum temperture is',df['temperature'].min())
# !to print the average value of the column
print('averagetemperture is',df['temperature'].mean())
# !to print the standard deviation of the column
print('standard deviation of temperture is',df['temperature'].std())
# !to print all the statistical value of all the integer valued columns
print('all the statistical values',df.describe())

# !set index(an integer index is an automatic index)
print("the index is:-")
print(df.index)
df.set_index('dates',inplace=True)
print(df)
print('**********')
print(df.loc['01/04/2017'])
df.reset_index(inplace=True)
print(df)