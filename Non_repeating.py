# Given list of integers
Given_list = [int(x) for x in input("Enter the list of number : ").split()]

# Create a dictionary to store the frequency of each element
n = {}

# Count the frequency of each element in the list
for num in Given_list:
    if num in n:
        n[num] += 1
    else:
        n[num] = 1

# Iterate through the list again to find the first non-repeating element
first_non_repeat = None
for num in Given_list:
    if n[num] == 1:
        first_non_repeating = num
        break

# Print the result
print("The first non-repeating element is :", first_non_repeating)
