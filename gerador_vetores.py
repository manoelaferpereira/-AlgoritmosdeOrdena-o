import random

def gerar_vetor(tipo, tamanho):
    if tipo == "melhor":
        return list(range(tamanho))
    elif tipo == "pior":
        return list(range(tamanho, 0, -1))
    else:
        vetor = list(range(tamanho))
        random.shuffle(vetor)
        return vetor
