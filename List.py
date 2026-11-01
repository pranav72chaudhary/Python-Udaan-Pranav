# List

li = ["Apple", "Mango", "Banana", "Orange", "Grapes", "Pineapple"]

print("Available fruits:", li)

print("First fruit:", li[0])

print("Last fruit:", li[-1])


# Append

# Append is used to add an element at the end of the list

li.append("Watermelon")

print("After adding a fruit:", li)


# Insert

# Insert is used to add an element at a specific position

li.insert(2, "Strawberry")

print("After inserting a fruit:", li)


# Pop

# Pop is used to remove an element from the list

li.pop(0)

print("After removing the first fruit:", li)


# Remove

# Remove is used to remove a specific element from the list

li.remove("Strawberry")

print("After removing Strawberry:", li)


# Slicing

print("Fruits from index 1 to 3:", li[1:4])

print("First five fruits:", li[:5])


# Extend

new_li = ["Kiwi", "Papaya"]

li.extend(new_li)

print("After adding more fruits:", li)