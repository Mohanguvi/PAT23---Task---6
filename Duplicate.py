# Given three lists
list1 = [61, 28, 53, 48, 56]
list2 = [33, 64, 93, 56, 72]
list3 = [56, 60, 67, 48, 94]

# Convert lists to sets
s1 = set(list1)
s2 = set(list2)
s3 = set(list3)

# intersection used to get the duplicates
duplicates = s1.intersection(s2, s3)

# Output the duplicates
if duplicates:
    print(f'Duplicates:', duplicates)
else:
    print('No duplicates found.')