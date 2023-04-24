import re #it is used for regular expression

A = 'Michael Jackson is the best'
B = A.upper()
print(B[0:5:2])

s1 = "Michael Jackson is the best"

# Define the pattern to search for
pattern = r"Jackson"

# Use the search() function to search for the pattern in the string
result = re.search(pattern, s1)

# Check if a match was found
if result:
    print("Match found!")
else:
    print("Match not found.")

# A simple example of using the \d special sequence in a regular expression pattern with Python code:
pattern = r"\d\d\d\d\d\d\d\d\d\d"  # Matches any ten consecutive digits
text = "My Phone number is 1234567890"
match = re.search(pattern, text)

if match:
    print("Phone number found:", match.group())
else:
    print("No match")

# A simple example of using the \W special sequence in a regular expression pattern with Python code:
pattern = r"\W"  # Matches any non-word character
text = "Hello, @world!"
matches = re.findall(pattern, text)

print("Matches:", matches)

# The findall() function finds all occurrences of a specified pattern within a string.

s2 = "Michael Jackson was a singer and known as the 'King of Pop'"


# Use the findall() function to find all occurrences of the "as" in the string
result = re.findall("as", s2)

# Print out the list of matched words
print(result)


# Split() Function split string into an array of substrings based on specified Pattern

# Use the split function to split the string by the "\s"
split_array = re.split("\s", s2)

# The split_array contains all the substrings, split by whitespace characters
print(split_array)

# The sub function of a regular expression in Python is used to replace all occurrences of a pattern in a string with a specified replacement.
# Define the regular expression pattern to search for
pattern = r"King of Pop"

# Define the replacement string
replacement = "legend"

# Use the sub function to replace the pattern with the replacement string
new_string = re.sub(pattern, replacement, s2, flags=re.IGNORECASE)

# The new_string contains the original string with the pattern replaced by the replacement string
print(new_string)