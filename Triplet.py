# Given list value and sum of the value is entered with a variable name of List and sum.
List = [20, 10, 30, 9]
sum = 59

# empty list of Triplte given to store the value of triplet of 59
Triplet = []

# Iterate through all possible combinations to find the three elements
for n1 in List:
    for n2 in List:
        for n3 in List:
            if n1 + n2 + n3 == sum: # check the combination of triplet whose sum equals to give value
                Triplet = [n1, n2, n3] # if found the value will be replaced in the triplet list.
# Result will be printed
if Triplet:
    print(f"Triplet value in list whose sum is equal to 59 is : {Triplet}")
else:
    print("No triplet vaue found in the list.")
