# Reading data from CSV in Python
import asyncio
from urllib import response

import pandas as pd

import urllib.request


# Define the URL of the CSV file
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv"

# Define the path where you want to save the CSV file
save_path = "addresses.csv" # C:/users/arqam.mirza/Desktop/data/addresses.csv

# Download the CSV file from the URL and save it to the specified path
urllib.request.urlretrieve(url, save_path)

# Read the CSV file using pandas
df = pd.read_csv(save_path)

# Print the first 5 rows of the CSV file
print(df.head())

# df = pd.read_csv("addresses.csv", header=None)

print(df)

# Adding column name to the DataFrame
# We can add columns to an existing DataFrame using its columns attribute.

df.columns =['First Name', 'Last Name', 'Location ', 'City','State','Area Code']

print(df)

# Selecting a single column
# To select the first column 'First Name', you can pass the column name as a string to the indexing operator.

print(df["First Name"])

# Selecting multiple columns
# To select multiple columns, you can pass a list of column names to the indexing operator.

df = df[['First Name', 'Last Name', 'City','State','Area Code']]
print(df)

# Selecting rows using .iloc and .loc
# Now, let's see how to use .loc for selecting rows from our DataFrame.
# loc() : loc() is label based data selecting method which means that we have to pass the name of the row or column which we want to select.

# To select the first row
print(df.loc[0])

# To select the 0th,1st and 2nd row of "First Name" column only
print(df.loc[[0,1,2], "First Name" ])

# To select the 0th,1st and 2nd row of "First Name" column only
print(df.iloc[[0,1,2], 0])

# Transform Function in Pandas
# Python’s Transform function returns a self-produced dataframe with transformed values after applying the function specified in its parameter.

#import library
import pandas as pd
import numpy as np

#creating a dataframe
df=pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
print(df)

# Let’s say we want to add 10 to each element in a dataframe:
#applying the transform function
df = df.transform(func = lambda x : x + 10)
print(df)

# Now we will use DataFrame.transform() function to find the square root to each element of the dataframe.

result = df.transform(func = ['sqrt'])
print(result)




# JSON file Format

import json

# Writing JSON to a File

person = {
    'first_name' : 'Mark',
    'last_name' : 'abc',
    'age' : 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}

# serialization using dump() function
# json.dump() method can be used for writing to JSON file.
# It is Dump
with open('person.json', 'w') as f:  # writing JSON object
    json.dump(person, f)

# it Dumps
# indent – defines the number of units for indentation

# Serializing json
json_object = json.dumps(person, indent=4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)

print(json_object)

# Reading JSON to a File

# Opening JSON file
with open('sample.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

print(json_object)
print(type(json_object))


# Reading Excel File .xlsx



import aiohttp
import pandas as pd
import asyncio

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx"
filename = "sample.xlsx"

# Download the file from the URL and save it to the local file system
urllib.request.urlretrieve(url, filename)

# Read the data from the file into a Pandas DataFrame
df = pd.read_excel(filename)