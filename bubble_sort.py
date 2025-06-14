def bubble_sort(lista):
    comparacoes = 0
    trocas = 0
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            comparacoes += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas += 1
    return lista, comparacoes, trocas
