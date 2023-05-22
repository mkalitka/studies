V = 20 #liczba wierzcholkow
# G[V] = lista_wierzcholkow
odwiedzone = [0] * V

def check_if_most(u, v):
    suma_prev = 0
    for i in range(V):
        if odwiedzone[i] == 0:
            DFS(i)
            suma_prev += 1

    while G[u].next != None:
        if G[u].next == v:
            G[u].next = G[u].next.next
        G[u] = G[u].next
    while G[v].next != None:
        if G[v].next == u:
            G[v].next = G[v].next.next
        G[v] = G[v].next

    odwiedzone = [0] * V

    suma_after = 0
    for i in range(V):
        if odwiedzone[i] == 0:
            DFS(i)
            suma_after += 1
    return suma_prev == suma_after


def DFS(w):
    odwiedzone[w] = 1
    while G[w] != None:
        new = G[w].val
        if(odwiedzone[new] == 0):
            DFS(new)
