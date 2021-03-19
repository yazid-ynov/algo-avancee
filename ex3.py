def ex3(lst):
    lst = set(lst)
    lst2 = []
    for x in lst:
        if x < 0:
            if x*(-1) not in lst2:
                lst2.append(x)
        else:
            if x * (-1) in lst2:
                lst2.pop(x * (-1))
                lst2.append(x)
            else:
                lst2.append(x)
    res = 0
    for x in lst2:
        res = res + x
    return res

# Driver program to test above function
print(ex3([-2, -5, 6, -2, -3, 1, 5, -6]))
