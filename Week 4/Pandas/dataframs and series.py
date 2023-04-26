# let us import the Pandas Library
import pandas as pd

#Define a dictionary 'x'

x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'],
      'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

#display the result df
print(df)

#Retrieving the "ID" column and assigning it to a variable x
x = df[['ID']]
print(x)

#check the type of x
print(type(x))

#Retrieving the Department, Salary and ID columns and assigning it to a variable z

z = df[['Department','Salary','ID']]
print(z)

# self practice

y = {'Student': ['David', 'Samuel', 'Terry', 'Evan'],
     'Age':['27', '24', '22', '32'],
     'Country':['UK', 'Canada', 'China', 'USA'],
     'Course':['Python', 'Data Structures', 'Machine Learning', 'Web Development'],
     'Marks': ['85', '72', '89', '76']}
dfy = pd.DataFrame(y)

# Printing of DataFrame

print(dfy)

# Retrieve the Marks column and assign it to a variable b

b=dfy[['Marks']]

# Printing Marks

print(b)

# Retrieve the Country and Course columns and assign it to a variable c

c = dfy[['Country', 'Course']]

# Printing Country and Marks

print(c)

# Get the Student column as a series Object

x = dfy['Student']
print(x)

# Data Collection Using loc (Lable-Base selecting Method) and iloc (Index-Based selecting Method)

# Access the value on the first row and the first column

print(dfy.iloc[0, 0])

# Access the value on the first row and the third column

print(dfy.iloc[0,2])

# Access the column using the name

print(dfy.loc[1, 'Marks'])

# Let us create a new dataframe called 'df2' and assign 'dfy' to it. Now, let us set the "Name" column as an index column using the method set_index().

df2=dfy
df2=df2.set_index("Student")

#To display the first 5 rows of new dataframe
print(df2.head())

#Now, let us access the column using the name
print(df2.loc['David', 'Marks'])

# let us do the slicing using old dataframe df

print(df.iloc[0:2, 0:3])

#let us do the slicing using loc() function on old dataframe df where index column is having labels as 0,1,2
print(df.loc[0:2,'ID':'Department'])

df2 = df
df2=df2.set_index("Name")

#let us do the slicing using loc() function on new dataframe df2 where index column is Name having labels: Rose, John and Jane
print(df2.loc['Rose':'Jane', 'ID':'Department'])