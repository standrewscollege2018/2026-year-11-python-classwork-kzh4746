''' This program demonstrates how to use a list '''

# Lists are used to store multiple pieces of info
# We use dquare brackets to show it is a list
names = ["Ace", "Chopper", "Luffy", "Nami", "Sanji", "Ussop", "Zoro"]

# Print the entire list
# This is useful for debugging
print(names)

# Each item has an index, its location in the list.
# The first item has an index of zero
# We can print individual items from a list by using their index
print(names[6])
# Using a negative index counts backwards from the end
# -1 prints the last item, -2 the second to last, etc
print(names[-1])
# If you put [:2] it prints all the names up to the second one
print(names[:2])

# We can use len() to get the number of items in a list
length = len(names)
# Here we print out the length of an item in the list
print(len(names[0]))

# To change an item, just overwrite it by setting a new value for that position in the list
names[4] = "White Beard"
print(names)

# You can insert into a particular position in a list
names.insert(1, "Sanji")
print(names)

# The most common method of adding items is to add them at the end using append()
names.append("Robin")
print(names)

# When displaying all items from a list it is best to use a loop rather than printing the whole list with brackets and commas
# Method 1: displaying each time
for name in names:
    print(name)

# Method 2: displaying items in a numbered list
for i in range(len(names)):
    print(f"{i+1}. {names[i]}")

# You can put spaces inbetween stuff
for i in range(len(names)):
    print(f"{i+1}. {names[i]:15} ikr")