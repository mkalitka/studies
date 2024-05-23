# https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/
# a)
def lis_better(arr):
    # wyliczanie
    n = len(arr)
    dp = [1]*n  
    for i in range(1, n):
        for j in range(0, i):
            if (arr[i] > arr[j] and dp[i] < dp[j] + 1):  # sprawdzamy czy opłaca nam się wydłużyć podciąg z dp[j] o element z i-tego pola
                dp[i] = dp[j]+1  # zmieniamy długość podciągu kończącego się w 
    # odzyskiwanie
    path = []                   # stos do odtwarzania listy od tyłu
    cur_len = max(dp)
    j = dp.index(cur_len) 
    prev_val = float('inf')
    while cur_len > 0:
        if dp[j] == cur_len and arr[j] < prev_val:
            path.append(arr[j])
            prev_val = arr[j]
            cur_len -= 1
        j -= 1
    return path[::-1]

print(lis_better([2, 7, 8, 4, 10, 3, 5, 6]))
# poprawne maxciągi
# --1----2----3---2---4----2---3-----4---=dp
# [[2], [7], [8], 4, [10], 3,  5,    6]
# [[2],  7,   8, [4], 10,  3,  [5], [6]]
# [[2],  7,   8,  4,  10, [3], [5], [6]]
print(lis_better([7, 1, 2, 8, 5]))
# poprawne maxciągi
# -1---1----2----3---3---=dp
# [7, [1], [2], [8], 5]
# [7, [1], [2],  8, [5]]

# https://www.geeksforgeeks.org/number-of-longest-increasing-subsequences/
# b)
def count_all_lis(arr):
    # wyliczanie bez zmian
    n = len(arr)
    dp = [1]*n  
    for i in range(1, n):
        for j in range(0, i):
            if (arr[i] > arr[j] and dp[i] < dp[j] + 1): 
                dp[i] = dp[j]+1
    # zliczanie:
    # dp_restore[i] = ile podciągów długości dp[i] z elementów arr[0..i] kończących się na arr[i] da się zbudować?
    dp_restore = [0]*n # domyślnie ustawiamy na 0
    # base: dla wszystkich zakończeń ciągów jednoelementowych ustawiamy długość na 1 
    # (no bo zawsze istnieje tylko 1 ciąg jednoelementowy kończący się daną liczbą)
    for i in range(n):
        if dp[i] == 1:
            dp_restore[i] = 1
    # dla każdej liczy arr[i] będącej końcem podciągu długości dp[i]...
    for i in range(1, n):
        # sprawdzamy, ile ciągów (długości dp[i]-1) może ona zakończyć (czyli jest większa niż ich ostatni wyraz)
        for j in range(0, i):
            if dp[j] == dp[i]-1 and arr[j] < arr[i]: 
                dp_restore[i] += dp_restore[j]

    # przechodzę po wszystkich końcach ciągów maksymalnej długości i zliczam, ile ciągów one zakańczają
    sum = 0
    for i in range(n):
        if dp[i] == max(dp):
            sum += dp_restore[i]
    return sum
    
    
print(count_all_lis([2, 7, 8, 4, 10, 3, 5, 6]))
# poprawne maxciągi
# --1----2----3---2---4----2---3-----4---=dp
# [[2], [7], [8], 4, [10], 3,  5,    6]
# [[2],  7,   8, [4], 10,  3,  [5], [6]]
# [[2],  7,   8,  4,  10, [3], [5], [6]]
print(count_all_lis([7, 1, 2, 8, 5]))
# poprawne maxciągi
# -1---1----2----3---3---=dp
# [7, [1], [2], [8], 5]
# [7, [1], [2],  8, [5]]
