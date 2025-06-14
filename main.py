#aquii Coordena os testes e salva os resultados
import sys
import os
import csv

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from algoritmos import bubble_sort, improved_bubble_sort, insertion_sort, selection_sort, merge_sort, quick_sort, heap_sort
from gerador_vetores import gerar_vetor
from avaliador import medir

algoritmos = [
    ("Bubble Sort", bubble_sort),
    ("Improved Bubble Sort", improved_bubble_sort),
    ("Insertion Sort", insertion_sort),
    ("Selection Sort", selection_sort),
    ("Merge Sort", merge_sort),
    ("Quick Sort", quick_sort),
    ("Heap Sort", heap_sort),
]

casos = ["melhor", "medio", "pior"]
tamanhos = [1000, 10000, 100000]

with open("resultados.csv", mode="w", newline="") as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(["Algoritmo", "Tamanho", "Tipo", "Tempo", "Comparacoes", "Trocas"])

    for nome, func in algoritmos:
        for tamanho in tamanhos:
            for caso in casos:
                print(f"Executando {nome} | Tamanho: {tamanho} | Caso: {caso}...")
                vetor = gerar_vetor(caso, tamanho)
                tempo, comparacoes, trocas = medir(func, vetor)
                writer.writerow([nome, tamanho, caso, round(tempo, 6), comparacoes, trocas])
                print(f"Concluído: Tempo={round(tempo, 6)}s, Comparações={comparacoes}, Trocas={trocas}\n")

print("Todos os testes foram concluídos. Resultados salvos em 'resultados.csv'.")
import time

def medir(algoritmo, vetor):
    inicio = time.time()
    _, comparacoes, trocas = algoritmo(vetor.copy())
    fim = time.time()
    return fim - inicio, comparacoes, trocas
