def insertion_sort(vetor):
    comparacoes = 0
    trocas = 0
    for i in range(1, len(vetor)):
        chave = vetor[i]
        j = i - 1
        while j >= 0:
            comparacoes += 1
            if vetor[j] > chave:
                vetor[j + 1] = vetor[j]
                trocas += 1
                j -= 1
            else:
                break
        vetor[j + 1] = chave
        trocas += 1
    return vetor, comparacoes, trocas