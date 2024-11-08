#SECTION 1
fruit_tuple = ("apple", "banana", "cherry", "date")
print(fruit_tuple[0])
# Print the last element
print(fruit_tuple[-1])
slice_tuple = fruit_tuple[1:3]  # Slicing from index 1 to 2 (3-1)
print(slice_tuple)

#SECTION 2
# Create num_tuple as per instruction
num_tuple = (1, 2, 2, 3, 4, 2, 5)
# Use the count method to count occurrences of 2
count_2 = num_tuple.count(2)
print(f"The number 2 appears {count_2} times in the tuple.")
# Use the index method to find the first occurrence of 4
index_4 = num_tuple.index(4)
print(f"The first occurrence of 4 is at index {index_4}.")

#SECTION 3
# Create person_info tuple
person_info = ("Latrell", "Clark", 17, "New York")
# Unpack the tuple
first_name, last_name, age, city = person_info
# Print the variables
print(f"Name: {first_name} {last_name}")
print(f"Age: {age}")
print(f"City: {city}")
