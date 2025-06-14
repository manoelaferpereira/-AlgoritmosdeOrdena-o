def quick_sort(vetor):
    comparacoes = 0
    trocas = 0

    def quick_sort_rec(v):
        nonlocal comparacoes, trocas
        if len(v) <= 1:
            return v
        pivo = v[len(v) // 2]
        menores = []
        iguais = []
        maiores = []
        for x in v:
            comparacoes += 1
            if x < pivo:
                menores.append(x)
            elif x == pivo:
                iguais.append(x)
            else:
                maiores.append(x)
                trocas += 1
        return quick_sort_rec(menores) + iguais + quick_sort_rec(maiores)

    return quick_sort_rec(vetor), comparacoes, trocas