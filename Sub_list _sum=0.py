
def sub_list(l10, l):
    for i in range(l - 1):
        s = l10[i]
        for j in range(i + 1, l):
            s += l10[j]
            if s == 0:
                return l10[i:j+1]
    return False

l10 = [4, 2, -3, 1, 6]

result = sub_list(l10, len(l10))
print("The sub-list value sum of equal is:", result)


