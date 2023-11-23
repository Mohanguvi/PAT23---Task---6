# Given number in the list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Empty list to store prime numbers
prime_numbers = []

# Iterate through each number in the given list
for prime in numbers:
    # Check if the number is greater than 1 and if it is a prime or not
    if prime > 1:
        '''loop to check the number is divisible by any other integer from 2 to 
        square root of the number(round upto nearst integer)'''
        for i in range(2, int(prime**0.5) + 1): 
            if prime % i == 0: #if the number is divisible by 0, then it is a prime number
                break
        else:
            # Adding the prime number to the prime_numbers list
            prime_numbers.append(prime)

# Print the list of prime numbers
print("Prime numbers in the list:", prime_numbers)
