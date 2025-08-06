def swap(tab, i, j):
    """Échange la place des éléments aux indices i et j du tableau"""
    tab[i], tab[j] = tab[j], tab[i]

    
def bubble(A):

    """Trie le tableau en déplaçant les plus grosses valeurs vers la fin du
    tableau, un peu comme des bulles dans l'eau qui remonteraient à la
    surface"""

    n = len(A)
    for i in range(n):
        for j in range(0, n-i-1):
            if A[j] > A[j+1]:
                swap(A, j, j+1)
    return A


def insertion(A):
    """Trie le tableau en plaçant l'élément courant à la bonne place dans
    le sous-tableau déjà trié"""
    
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i
        while j > 0 and A[j-1] > key:
            A[j] = A[j-1]
            j -= 1
        A[j] = key
    return A


def selection(A):
    """Trie le tableau en cherchant le plus petit élément à mettre dans la
    première case, puis le second plus petit à mettre dans la seconde case,
    etc"""
    
    n = len(A)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if A[j] < A[min_index]:
                min_index = j
        swap(A, i, min_index)
    return A