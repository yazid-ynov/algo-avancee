def ex4(lst1, lst2):
    for word in lst1:
        lst22 = set(lst2)
        check = 1
        for c in word:
            if c not in lst22:
                check = 0
                break
            else:
                lst22.remove(c)
        if check == 1:
            print(word)



# tester le programme

words = ["go","bat","me","eat","goal","boy", "run"]
chars = ['e','o','b','a','m','g','l']

ex4(words, chars)

# Calcul d complaxite d algo
""" 
T(n) = n(2+n(5)) = O(n^2) 
"""
