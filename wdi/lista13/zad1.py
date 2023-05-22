class ListItem:
    def __init__(self, value):
        self.val = value
        self.next = None

def matrix_to_list(m, n):
    lista_list = [0] * n
    for i in range(n):
        l = None
        for j in range(n):
            if m[i][j] == 1:
                l = ListItem(j)
                l = l.next
        lista_list[i] = l
    return lista_list

def list_to_matrix(l, n):
    m = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        while l[i] != None:
            m[i][l[i].val] = 1
    return m
