def heap_sort(vetor):
    import heapq
    comparacoes = len(vetor) * 2  
    trocas = len(vetor)           
    heapq.heapify(vetor)
    return [heapq.heappop(vetor) for _ in range(len(vetor))], comparacoes, trocas