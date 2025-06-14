#Mede tempo, comparações e trocas de um algoritmoo
import time

def medir(algoritmo, vetor):
    inicio = time.time()
    _, comparacoes, trocas = algoritmo(vetor.copy())
    fim = time.time()
    return fim - inicio, comparacoes, trocas
