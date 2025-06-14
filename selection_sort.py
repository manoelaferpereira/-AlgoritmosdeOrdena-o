def selection_sort(vetor):
    comparacoes = 0
    trocas = 0
    n = len(vetor)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparacoes += 1
            if vetor[j] < vetor[min_idx]:
                min_idx = j
        if min_idx != i:
            vetor[i], vetor[min_idx] = vetor[min_idx], vetor[i]
            trocas += 1
    return vetor, comparacoes, trocas