import requests
import os
from PIL import Image
from IPython.display import IFrame

# You can make a GET request via the method get to www.ibm.com:

url='https://www.ibm.com/'
r=requests.get(url)

# We have the response object r, this has information about the request, like the status of the request. We can view the status code using the attribute status_code.

r.status_code

# You can view the request headers:

print(r.request.headers)

# You can view the request body, in the following line, as there is no body for a get request we get a None:

header=r.headers
print(r.headers)

# We can obtain the date the request was sent using the key Date

header['date']

# Content-Type indicates the type of data:

header['Content-Type']

# You can also check the encoding:

r.encoding

# As the Content-Type is text/html we can use the attribute text to display the HTML in the body. We can review the first 100 characters:

r.text[0:100]

# You can load other types of data for non-text requests, like images. Consider the URL of the following image:

# Use single quotation marks for defining string
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
print(r.headers)

r.headers['Content-Type']

# An image is a response object that contains the image as a bytes-like object. As a result, we must save it using a file object. First, we specify the file path and

path=os.path.join(os.getcwd(),'image.png')
print(path)

# We save the file, in order to access the body of the response we use the attribute content then save it using the open function and write method:

with open(path,'wb') as f:
    f.write(r.content)

# We can view the image:

# Image.open(path) // Has image error


# Get Request with URL Parameters
# The Base URL is for http://httpbin.org/ is a simple HTTP Request & Response Service. The URL in Python is given by:

url_get='http://httpbin.org/get'

# To create a Query string, add a dictionary. The keys are the parameter names and the values are the value of the Query string.

payload={"name":"Joseph","ID":"123"}

# Then passing the dictionary payload to the params parameter of the  get() function:

r=requests.get(url_get,params=payload)

# Print URL

print(r.url)

# There is no request body

print("request body:", r.request.body)

# We can print out the status code

print(r.status_code)

# We can view the response as text:

print(r.text)

# We can look at the 'Content-Type'.

r.headers['Content-Type']

# As the content 'Content-Type' is in the JSON format we can use the method json(), it returns a Python dict:
print('Jason Started')
print(r.json())

# The key args has the name and values:
print('Jason Args')
print(r.json()['args'])


# Post Request

# Like a GET request, a POST is used to send data to a server, but the POST request sends the data in a request body. In order to send the Post Request in Python, in the URL we change the route to POST:

url_post='http://httpbin.org/post'

# To make a POST request we use the post() function, the variable payload is passed to the parameter  data :

r_post=requests.post(url_post,data=payload)

# Comparing the URL from the response object of the GET and POST request we see the POST request has no name or value pairs.

print("POST request URL:",r_post.url )
print("GET request URL:",r.url)

# We can compare the POST and GET request body, we see only the POST request has a body:

print("POST request body:",r_post.request.body)
print("GET request body:",r.request.body)

# We can view the form as well:
print('Jason Form')
print(r_post.json()['form'])