def ex5(set, n, sum):
    # Base Cases
    if (sum == 0):	return True
    if (n == 0 and sum != 0):	return False
    # si un element est sup ignore le
    if (set[n - 1] > sum):
        return ex5(set, n - 1, sum);
    # else, check si c possible
    return ex5(set, n - 1, sum) or ex5(set, n - 1, sum - set[n - 1])


# tester le programme
set =  [3, 34, 4, 12, 5, 2]
sum = 9
n = len(set)
if (ex5(set, n, sum) == True):
    print("Found a subset")
else:
    print("No")
