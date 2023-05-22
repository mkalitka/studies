def poj_sum(list, a):
    suma = 0
    for i in list:
        try:
            suma += i[a]
        except IndexError:
            pass
    return suma

def somesum(list):
    return [poj_sum(list, i) for i in range(len(max(list)))]
    

print(somesum([[2, 4, 7, 0, -3], [2, 1, 6, 3], [5, 8, -2, 0, 1, 3], [1, 6, 3, 7, 8, 3]]))
