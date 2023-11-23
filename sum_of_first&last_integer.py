# Get an integer value from the user
num = int(input("Enter an integer: "))

# Convert the integer into a string to easily extract digits
n_str = str(num)

# Get the first and last digits using slicing function
fdigit = int(n_str[0])
ldigit = int(n_str[-1])

# Calculating the sum of the first and last digits
sum = fdigit + ldigit

# print the result
print(f"The sum of first and last digits of {num} is: {sum}")