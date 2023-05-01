from randomuser import RandomUser
import pandas as pd

r = RandomUser()

# Then, using generate_users() function, we get a list of random 10 users.

some_list = r.generate_users(10)

print(some_list)

# The "Get Methods" functions mentioned at the beginning of this notebook, can generate the required parameters to construct a dataset. For example, to get full name, we call get_full_name() function.

name = r.get_full_name()

# Let's say we only need 10 users with full names and their email addresses. We can write a "for-loop" to print these 10 users.

for user in some_list:
    print (user.get_full_name()," ",user.get_email())

# generate photos of the random 5 users.
for user in some_list:
    print (user.get_picture())

# To generate a table with information about the users, we can write a function containing all desirable parameters. For example, name, gender, city, etc. The parameters will depend on the requirements of the test to be performed. We call the Get Methods, listed at the beginning of this notebook. Then, we return pandas dataframe with the users.

def get_users():
    users = []

    for user in RandomUser.generate_users(10):
        users.append({"Name": user.get_full_name(), "Gender": user.get_gender(), "City": user.get_city(),
                      "State": user.get_state(), "Email": user.get_email(), "DOB": user.get_dob(),
                      "Picture": user.get_picture()})

    return pd.DataFrame(users)

get_users()

df1 = pd.DataFrame(get_users())

print(df1)

# Another, more common way to use APIs, is through requests library. The next lab, Requests and HTTP, will contain more information about requests.

# We will start by importing all required libraries.

import requests
import json

# We will obtain the fruitvice API data using requests.get("url") function. The data is in a json format.

data = requests.get("https://fruityvice.com/api/fruit/all")

# We will retrieve results using json.loads() function.

results = json.loads(data.text)

# We will convert our json data into pandas data frame.

pd.DataFrame(results)

# The result is in a nested json format. The 'nutrition' column contains multiple subcolumns, so the data needs to be 'flattened' or normalized.

df2 = pd.json_normalize(results)
print(df2)

# Let's see if we can extract some information from this dataframe. Perhaps, we need to know the family and genus of a cherry.

cherry = df2.loc[df2["name"] == 'Cherry']
print((cherry.iloc[0]['family']) , (cherry.iloc[0]['genus']))
