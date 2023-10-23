def max_sublist_sum(lista: list):
    max_sum = 0
    max_i = 0
    max_j = 0
    for i in range(len(lista)):
        for j in range(i, len(lista)):
            sub_sum = sum(lista[i : j + 1])
            if sub_sum > max_sum:
                max_sum = sub_sum
                max_i = i
                max_j = j
    return (max_i, max_j)


print(max_sublist_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(max_sublist_sum([1, -2, 3, 4, 5, -6, 7, 8, 9, 10]))
print(max_sublist_sum([1, -2, 3, 4, 5, -6, 7, 8, 9, -10]))
