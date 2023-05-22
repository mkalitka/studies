def count_hiper_happy(range_digits=10, sevens_amount=7):
    if range_digits < sevens_amount:
        return 0
    free_places = range_digits - sevens_amount
    return 10 ** free_places + free_places * (10 ** free_places - 10 ** (free_places - 1))

print(count_hiper_happy())
