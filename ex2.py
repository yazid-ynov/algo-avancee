
def clean(matrice, i, j):
    if i < 0 or j < 0 or i >= len(matrice) or j >= len(matrice[0]) or matrice[i][j] == 0 or matrice[i][j] == 2:
        return
    if (matrice[i][j] == 1):
        matrice[i][j] = 2
    else:
        return
    clean(matrice, i-1, j)
    clean(matrice, i, j-1)
    clean(matrice, i, j+1)
    clean(matrice, i+1, j)
    clean(matrice, i + 1, j +1)
    clean(matrice, i + 1, j -1)
    clean(matrice, i - 1, j +1)
    clean(matrice, i - 1, j-1)

def ex2_numIslands(matrice):
    res = 0
    r = len(matrice)
    c = len(matrice[0])

    for i in range(r - 1):
        for j in range(c - 1):
            if (matrice[i][j] == 1):
                res += 1
                clean(matrice, i, j)
    return res

# tester l programme
matrice = [
 [1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
 [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
 [1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
 [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
 [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
 [0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
 [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
 [0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
 [1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
 [1, 1, 1, 1, 0, 0, 0, 1, 1, 1]
]
print(ex2_numIslands(matrice))
