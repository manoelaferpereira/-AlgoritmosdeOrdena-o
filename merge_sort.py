def merge_sort(vetor):
    comparacoes = 0
    trocas = 0

    def merge_sort_rec(v):
        nonlocal comparacoes, trocas
        if len(v) <= 1:
            return v
        meio = len(v) // 2
        esquerda = merge_sort_rec(v[:meio])
        direita = merge_sort_rec(v[meio:])

        resultado = []
        i = j = 0
        while i < len(esquerda) and j < len(direita):
            comparacoes += 1
            if esquerda[i] <= direita[j]:
                resultado.append(esquerda[i])
                i += 1
            else:
                resultado.append(direita[j])
                j += 1
                trocas += 1
        resultado.extend(esquerda[i:])
        resultado.extend(direita[j:])
        return resultado

    return merge_sort_rec(vetor), comparacoes, trocas