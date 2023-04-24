# Create a set

set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
print(set1)

# Convert list to set

album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", \
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)
print(album_set)

# Convert list to set

music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul", \
                    "progressive rock", "soft rock", "R&B", "disco"])
print(music_genres)

# Sample set

A = set(["Thriller", "Back in Black", "AC/DC"])
print(A)

# Add element to set

A.add("NSYNC")
print(A)

# Try to add duplicate element to the set

A.add("NSYNC")
print(A)

# Remove the element from set

A.remove("NSYNC")
print(A)

# Verify if the element is in the set

if "AC/DC" in A:
    print("Yes AC/DC in Set")
else:
    print("No")

# Sample Sets

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

# Print two sets

print(album_set1, album_set2)

# Find the intersections

intersection = album_set1 & album_set2
print(intersection)

# Find the difference in set1 but not set2

print(album_set1.difference(album_set2))

# Use intersection method to find the intersection of album_list1 and album_list2

print(album_set1.intersection(album_set2))

# Find the union of two sets

print(album_set1.union(album_set2))

# Check if superset
if set(album_set1).issuperset(album_set2):
    print("Yes!")
else:
    print("No!")

# Check if subset

if set(album_set2).issubset(album_set1):
    print("Yes!")
else:
    print("No!")

# Check if subset

if set({"Back in Black", "AC/DC"}).issubset(album_set1):
    print("Yes!")
else:
    print("No!")

# Check if superset

if album_set1.issuperset({"Back in Black", "AC/DC"}):
    print("Yes!")
else:
    print("No!")