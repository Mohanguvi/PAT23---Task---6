# distribute_mangoes function used to define this code
def distribute_mangoes(N, M):
    # Sorting the list of mangoes in ascending order
    N.sort() 
    
    # Hold the minium and minimum value of the Mango N list
    min_mangoes = N[0]
    max_mangoes = N[-1]

     # Ensure the difference between the maximum and minimum mangoes is less than or equal to 1
    while max_mangoes - min_mangoes > 1 and M > 1:
        # Distributing the mangoes to get the less difference of 1
        N[0] += 1
        N[-1] -= 1
        N.sort()
        max_mangoes = N[-1]
        min_mangoes = N[0]
        M -= 1
    difference = max_mangoes - min_mangoes

    return difference
# Get the user input value of list N and M, difference value is printed:
N = [int(x) for x in input("Enter the list of number of Mangoes in a bag N: ").split()]
M = int(input("Enter the number of students M: "))
result = distribute_mangoes(N, M)
print(f"Difference between the maximum and minimum number of mangoes in the bag: {result}")
