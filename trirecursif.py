import random

def generate_random_array(debug=False, N=21):
    """Renvoie un tableau contenant toutes les valeurs entières de 0 (inclus)
    à N (exclus) rangées dans un ordre aléatoire

    Args:
        debug (boolean): quand debug est vrai, la fonction renvoie toujours le
                         même tableau afin de simplifier le débogage de vos
                         algorithmes de tri
        N (int): la taille du tableau à renvoyer

    Returns:
        list[int]: un tableau d'entiers, de taille N, non ordonné
    """

    if debug:
        return [3, 9, 7, 1, 6, 2, 8, 4, 5, 0]

    array = list(range(0, N))
    random.shuffle(array)

    return array


# Exemple d'utilisation de la fonction precedente

print(generate_random_array()) # Retourne un tableau avec des nombres naturels allant de 0 a 20
print(generate_random_array(True)) # Retourne le tableau [3, 9, 7, 1, 6, 2, 8, 4, 5, 0]
print(generate_random_array(N=31)) # Des nombres naturels allant de 0 a 30

def swap(tab, i, j):
    """Échange la place des éléments aux indices i et j du tableau"""
    
    raise NotImplementedError


def bubble(A):
    """Trie le tableau en déplaçant les plus grosses valeurs vers la fin du
    tableau, un peu comme des bulles dans l'eau qui remonteraient à la
    surface"""

    raise NotImplementedError


bubble(generate_random_array())


def insertion(A):
    """Trie le tableau en plaçant l'élément courant à la bonne place dans
    le sous-tableau déjà trié"""

    raise NotImplementedError


insertion(generate_random_array())

def selection(A):
    """Trie le tableau en cherchant le plus petit élément à mettre dans la
    première case, puis le second plus petit à mettre dans la seconde case,
    etc"""
    
    raise NotImplementedError

selection(generate_random_array())