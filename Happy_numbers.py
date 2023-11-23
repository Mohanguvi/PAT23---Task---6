# Given list to find the happy numbers
my_list = [10, 501, 22, 37, 100, 999, 87, 351]

# To store the value emply list is given
count = []

def happy(my_list): #Happy function to check the given number are happy numbers or not
    for i in range(len(my_list)): #iterative through the each number in the given list 
        sum = my_list[i]
        while sum != 1 and sum != 4: # loop continues until the either the sum becomes 1(Happy number) or 4(Not happy number)
            tsum = 0
            for digit in str(sum): 
                tsum += int(digit)**2 # nested loop calculates the sum of the squares of the digits for the current number
            sum = tsum  
        if sum == 1:
            count.append(my_list[i]) # if it is happy number then it will be added in the count[]
    return count 

print("Happy numbers in the given list are:", happy(my_list))

