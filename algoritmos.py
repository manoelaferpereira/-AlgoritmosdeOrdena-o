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

def improved_bubble_sort(lista):
    comparacoes = 0
    trocas = 0
    n = len(lista)
    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            comparacoes += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
                trocas += 1
        if not trocou:
            break
    return lista, comparacoes, trocas

def insertion_sort(lista):
    comparacoes = 0
    trocas = 0
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            comparacoes += 1
            lista[j + 1] = lista[j]
            trocas += 1
            j -= 1
        comparacoes += 1 if j >= 0 else 0
        lista[j + 1] = chave
    return lista, comparacoes, trocas

def selection_sort(lista):
    comparacoes = 0
    trocas = 0
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparacoes += 1
            if lista[j] < lista[min_idx]:
                min_idx = j
        if min_idx != i:
            lista[i], lista[min_idx] = lista[min_idx], lista[i]
            trocas += 1
    return lista, comparacoes, trocas

def merge_sort(lista):
    comparacoes = 0
    trocas = 0

    def merge_sort_rec(lst):
        nonlocal comparacoes, trocas
        if len(lst) <= 1:
            return lst
        meio = len(lst) // 2
        esquerda = merge_sort_rec(lst[:meio])
        direita = merge_sort_rec(lst[meio:])
        return merge(esquerda, direita)

    def merge(esq, dir):
        nonlocal comparacoes, trocas
        resultado = []
        i = j = 0
        while i < len(esq) and j < len(dir):
            comparacoes += 1
            if esq[i] <= dir[j]:
                resultado.append(esq[i])
                i += 1
            else:
                resultado.append(dir[j])
                j += 1
                trocas += 1
        resultado.extend(esq[i:])
        resultado.extend(dir[j:])
        return resultado

    lista_ordenada = merge_sort_rec(lista)
    return lista_ordenada, comparacoes, trocas

def quick_sort(lista):
    comparacoes = 0
    trocas = 0

    def quick_sort_rec(lst):
        nonlocal comparacoes, trocas
        if len(lst) <= 1:
            return lst
        pivo = lst[0]
        menores = []
        maiores = []
        for x in lst[1:]:
            comparacoes += 1
            if x < pivo:
                menores.append(x)
            else:
                maiores.append(x)
        trocas += len(menores) + len(maiores)
        return quick_sort_rec(menores) + [pivo] + quick_sort_rec(maiores)

    lista_ordenada = quick_sort_rec(lista)
    return lista_ordenada, comparacoes, trocas

def heap_sort(lista):
    comparacoes = 0
    trocas = 0
    n = len(lista)

    def heapify(n, i):
        nonlocal comparacoes, trocas
        maior = i
        esquerda = 2 * i + 1
        direita = 2 * i + 2

        if esquerda < n:
            comparacoes += 1
            if lista[esquerda] > lista[maior]:
                maior = esquerda

        if direita < n:
            comparacoes += 1
            if lista[direita] > lista[maior]:
                maior = direita

        if maior != i:
            lista[i], lista[maior] = lista[maior], lista[i]
            trocas += 1
            heapify(n, maior)

    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        trocas += 1
        heapify(i, 0)

    return lista, comparacoes, trocas
