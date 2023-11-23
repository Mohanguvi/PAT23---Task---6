# Given list is entered in a list
L = [10, 501, 22, 37, 100, 999, 87, 351]

# two empty lists of even and odd to store the value from the List.
even_number = []
odd_number = []

for num in L:  #for loop to iterartive through each value in the Given_list.
    if num % 2 == 0:     #checks whether the number is even or odd.
        even_number.append(num)  #if it is even append command will add the value in even list.
    else:
        odd_number.append(num)   #if it is odd append command will add the value in odd list.

# Results will be printed to display the even and odd numbers.
print("Even numbers:", even_number)
print("Odd numbers:", odd_number)