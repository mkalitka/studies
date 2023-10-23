def sudan(n, x, y):
    if n == 0:
        return x + y
    elif y == 0:
        return x
    else:
        return sudan(n - 1, sudan(n, x, y - 1), sudan(n, x, y - 1) + y)


memo = {}


def sudan_memo(n, x, y):
    if (n, x, y) in memo:
        return memo[(n, x, y)]

    if n == 0:
        result = x + y
    elif y == 0:
        result = x
    else:
        result = sudan(n - 1, sudan(n, x, y - 1), sudan(n, x, y - 1) + y)

    memo[(n, x, y)] = result

    return result


if __name__ == "__main__":
    print(sudan(2, 1, 2))
    print(sudan_memo(2, 1, 2))
