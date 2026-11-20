my_list = [76, 92.3, "hello", True, 4, 76]

# Append "apple" and 76 to the list
my_list.append("apple")
my_list.append(76)

# Insert the value "cat" at position (index) 3
my_list.insert(3, "cat")

# Insert the value 99 at the start of the list
my_list.insert(0, 99)

# Find the index of "hello"
hello_index = my_list.index("hello")

# Count the number of 76s in the list
count_76 = my_list.count(76)

# Remove the first occurrence of 76 from the list
my_list.remove(76)

# Remove True from the list using pop and index
my_list.pop(my_list.index(True))