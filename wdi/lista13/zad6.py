def check_if_art_point(G, v):
    t = G[v].next
    if t == None:
        return True
    while t != None:
        if check_if_most(G, v, t.val):
            return True
        t = t.next
    return False
