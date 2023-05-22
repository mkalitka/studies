def check_if_most_exists(g, n):
    for i in range(n):
        k = g[i]
        while k != None:
            if check_if_most(g, i, k.val) == True:
                return True
            else:
                k = k.next
    return False
