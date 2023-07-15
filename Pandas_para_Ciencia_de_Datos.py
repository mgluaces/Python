## Data Structures  in Pandas

import pandas as pd
import numpy as np

#Creating a Series from a list
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print (series)

# Creating a DataFrame from a  dictionary
data = {'Name': ['John', 'Jane', 'Mike'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'París']}
df = pd.DataFrame(data)
print(df)

# Creating a Panel from a three-dimensional NumPy array
data = np.random.rand(3, 4, 5)
panel = pd.Panel(data)
print(panel)

## Reading and Writing Data

import pandas as pd

# Reading a CSV file into a DataFrame
df = pd.read.csv('data.csv')

import pandas as pd

# Writing a DataFrame to a CSV file
df.to_csv('output', index=False)

import pandas as pd

# Reading an Excel file into a DataFrame
df = pd.read_excel('data.xlsx')
print(df)

import pandas as pd

# Writing a DataFrame to an Excel file
df.to_excel('output.xlsx', index=False)

## Data Manipulation

import pandas as pd

# Selecting a single column
col = df['Column_Name']

# Selecting  multiple columns
cols = df[['Column1', 'Column2']]

import pandas as pd

# Selecting rows based on conditions
selected_rows = df[df['Column_Name'] > 50]

# Selecting rows by their position
selected_rows = df.iloc[2:5]

import pandas as pd

# Filtering data based on a condition
filtered_data = df[df['Column_Name'] > 50]

import pandas as pd

# Sorting data based on a single column
sorted_data = df.sort_values('Column_Name')

# Sorting data based on multiple columns
sorted_data = df.sort_values (['Column1', 'Column2'])

import pandas as pd

# Calculating the sum of a column
column_sum = df['Column_Name'].sum()

# Calculating the  mean of a column
column_mean =  df['Column_Name'].mean()

# Counting the number of occurrences in a column
column_count = df['Column_Name'].value_counts()

import pandas as pd

# Dropping rows with missing values
clean_data = df.dropna()

# Filling missing values with a specific value
filled_data = df.fillna(0)

# Filling missing values with the mean of the column
mean_filled_data = df.fillna(df.mean())

## Data Cleaning

import pandas as pd

# Checking for duplicate rows
duplicate_rows = df.duplicated()

# Dropping duplicate rows
clean_data = df.drop_duplicates()

import pandas as pd

# Renaming columns
df.rename(columns={'Old_Name': 'New_Name'}, inplace=True)

import pandas as pd

# Checking for null values
null_values = df.isnull()

#  Dropping rows with null values
clean_data = df.dropna()

import pandas as pd

# Changing data type of a column
df['Column_Name'] = df['Column_Name'].astype(int)

## Data Visualization

import pandas as pd
import matplotlib.pyplot as plt

# Creating a line plot
df.plot(x='Date', y='Value')
plt.title('Line Plot')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Creating a bar plot
df.plot(kind='bar', x='Category', y='Value')
plt.title('Bar Plot')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Creating a scatter plot
df.plot(kind='scatter', x='X', y='Y')
plt.title('Scatter Plot')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Creating a histogram
df['Column_Name'].plot(kind='hist')
plt.title('Histogram')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Creating a box plot
df.boxplot(column='Value', by='Category')
plt.title('Box Plot')
plt.show()

## Time Series Analysis

import pandas as pd

# Creating a time series with a fixed frequency
dates = pd.date_range(start='2021-01-01', end='2021-12-31', freq='D')

import pandas as pd

# Resampling a time series to a lower frequency
weekly_data = df.resample('w').mean()

import pandas as pd

# Shifting time series data by a specified number of periods
shifted_data = df['Column_Name'].shift(i)

import pandas as pd

# Calculating the rolling mean over a window of size 3
rolling_mean = df['Column_Name'].rolling(window=3).mean()

'''
CONCLUSION

This practical guide has introduced you to the key features of Pandas 
for data science. You learned about installing Pandas,importing it into 
your Python environment, and working with itsdata structures, such as Series, 
DataFrame, and Panel. Youalso explored various data manipulation techniques, 
datacleaning methods, data visualization options, and time seriesanalysis 
capabilities in Pandas. With this knowledge, you canstart using Pandas 
effectively for your data science projects.

'''