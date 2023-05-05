from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page

html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

# To parse a document, pass it into the BeautifulSoup constructor, the BeautifulSoup object, which represents the document as a nested data structure:

soup = BeautifulSoup(html, "html.parser")

# We can use the method prettify() to display the HTML in the nested structure:

print(soup.prettify())

# Tags
# Let's say we want the title of the page and the name of the top paid player we can use the Tag. The Tag object corresponds to an HTML tag in the original document, for example, the tag title.

tag_object=soup.title
print("tag object:",tag_object)

# we can see the tag type bs4.element.Tag

print("tag object type:",type(tag_object))

# If there is more than one Tag with the same name, the first element with that Tag name is called, this corresponds to the most paid player:

tag_object=soup.h3
print(tag_object)

# Childern, Parents and Siblings
# As stated above the Tag object is a tree of objects we can access the child of the tag or navigate down the branch as follows:

tag_child =tag_object.b
print(tag_child)

# You can access the parent with the  parent

parent_tag=tag_child.parent
print(parent_tag)

# tag_object parent is the body element.

print(tag_object.parent)

# tag_object sibling is the paragraph element

sibling_1=tag_object.next_sibling
print(sibling_1)


# sibling_2 is the header element which is also a sibling of both sibling_1 and tag_object

sibling_2=sibling_1.next_sibling
print(sibling_2)

# HTML Attributes
# If the tag has attributes, the tag id="boldest" has an attribute id whose value is boldest. You can access a tag’s attributes by treating the tag like a dictionary:

print(tag_child['id'])

# You can access that dictionary directly as attrs:

print(tag_child.attrs)

# We can also obtain the content if the attribute of the tag using the Python get() method.

print(tag_child.get('id'))

# A string corresponds to a bit of text or content within a tag. Beautiful Soup uses the NavigableString class to contain this text. In our HTML we can obtain the name of the first player by extracting the sting of the Tag object tag_child as follows:

tag_string=tag_child.string
print(tag_string)

# we can verify the type is Navigable String

print(type(tag_string))

# A NavigableString is just like a Python string or Unicode string, to be more precise. The main difference is that it also supports some BeautifulSoup features. We can covert it to sting object in Python:

unicode_string = str(tag_string)
print(unicode_string)

# Filter Apply


table = "<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"

table_bs = BeautifulSoup(table, "html.parser")
print(table_bs)

# When we set the name parameter to a tag name, the method will extract all the tags with that name and its children.

table_rows=table_bs.find_all('tr')
print(table_rows)

# The result is a Python Iterable just like a list, each element is a tag object:

first_row =table_rows[0]
print(first_row)

# The tag type is

print(type(first_row))

# we can obtain the child

print(first_row.td)

# If we iterate through the list, each element corresponds to a row in the table:

for i, row in enumerate(table_rows):
    print("row", i, "is", row)

# As row is a cell object, we can apply the method find_all to it and extract table cells in the object cells using the tag td, this is all the children with the name td. The result is a list, each element corresponds to a cell and is a Tag object, we can iterate through this list as well. We can extract the content using the string attribute.

for i,row in enumerate(table_rows):
    print("row",i)
    cells=row.find_all('td')
    for j,cell in enumerate(cells):
        print('colunm',j,"cell",cell)

# If we use a list we can match against any item in that list.

list_input=table_bs .find_all(name=["tr", "td"])
# print(list_input)

#Attributes
# If the argument is not recognized it will be turned into a filter on the tag’s attributes. For example the id argument, Beautiful Soup will filter against each tag’s id attribute. For example, the first td elements have a value of id of flight, therefore we can filter based on that id value.

print(table_bs.find_all(id="flight"))

# We can find all the elements that have links to the Florida Wikipedia page:

list_input=table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
print(list_input)

# If we set the href attribute to True, regardless of what the value is, the code finds all tags with href value:

print(table_bs.find_all(href=True))

# String
# With string you can search for strings instead of tags, where we find all the elments with Florida:

print(table_bs.find_all(string="Florida"))

# Find

two_tables="<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"

# We create a BeautifulSoup object two_tables_bs

two_tables_bs= BeautifulSoup(two_tables, 'html.parser')

# We can find the first table using the tag name table

print(two_tables_bs.find("table"))

# We can filter on the class attribute to find the second table, but because class is a keyword in Python, we add an underscore.

print(two_tables_bs.find("table",class_='pizza'))

# Downloading And Scraping The Contents Of A Web Page
# We Download the contents of the web page:

url = "http://www.ibm.com"

# We use get to download the contents of the webpage in text format and store in a variable called data:

data  = requests.get(url).text

# print(data)

soup = BeautifulSoup(data,"html.parser")  # create a soup object using the variable 'data'

print(soup)

# Scrape all links

for link in soup.find_all('a',href=True):  # in html anchor/link is represented by the tag <a>

    print(link.get('href'))

# Scrape all images Tags

for link in soup.find_all('img'):# in html image is represented by the tag <img>
    print(link)
    print(link.get('src'))


# Scrap Data From HTML Tables

#The below url contains an html table with data about colors and color codes.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"

# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text

soup = BeautifulSoup(data,"html.parser")
print(soup)

#find a html table in the web page
table = soup.find('table') # in html table is represented by the tag <table>

#Get all rows from the table
for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td') # in html a column is represented by the tag <td>
    color_name = cols[2].string # store the value in column 3 as color_name
    color_code = cols[3].string # store the value in column 4 as color_code
    print("{}--->{}".format(color_name,color_code))

# Scrape data from HTML tables into a DataFrame using BeautifulSoup and Pandas

import pandas as pd
#The below url contains html tables with data about world population.
url = "https://en.wikipedia.org/wiki/World_population"

# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text
soup = BeautifulSoup(data,"html.parser")

#find all html tables in the web page
tables = soup.find_all('table') # in html table is represented by the tag <table>

print(tables)

# we can see how many tables were found by checking the length of the tables list
len(tables)

print(len(tables))

for index,table in enumerate(tables):
    if ("10 most densely populated countries" in str(table)):
        table_index = index
print(table_index)

# See if you can locate the table name of the table, 10 most densly populated countries, below.

print(tables[table_index].prettify())

# We can now use the pandas function read_html and give it the string version of the table as well as the flavor which is the parsing engine bs4.

print(pd.read_html(str(tables[5]), flavor='bs4'))

# The function read_html always returns a list of DataFrames so we must pick the one we want out of the list.

population_data_read_html = pd.read_html(str(tables[5]), flavor='bs4')[0]
print(population_data_read_html)
