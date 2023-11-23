# Get the user input list value
l = input("Enter the element by spaces: ")
list =l.split()

# sort the list in ascending order to get the minimum element
list.sort()

# print the result
print(" Smallest element in the list is : ",list[0])
