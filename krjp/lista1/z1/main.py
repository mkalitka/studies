from decimal import Decimal


def vat_faktura(lista):
    sum = 0
    for i in lista:
        sum += i
    try:
        sum = sum * 1.23
    except TypeError:
        sum = sum * Decimal("1.23")
    return sum


def vat_paragon(lista):
    try:
        lista = [i * 1.23 for i in lista]
    except TypeError:
        lista = [i * Decimal("1.23") for i in lista]
    sum = 0
    for i in lista:
        sum += i
    return sum


if __name__ == "__main__":
    # Lista cen, których faktura i paragon jest różna dla float
    zakupy = [3.23, 4.51, 5.02]
    print(vat_faktura(zakupy) == vat_paragon(zakupy))

    zakupy_dec = [Decimal(i) for i in zakupy]
    print(vat_faktura(zakupy_dec) == vat_paragon(zakupy_dec))

