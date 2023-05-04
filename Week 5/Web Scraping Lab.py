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