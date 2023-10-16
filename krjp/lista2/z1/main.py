def dhondt(results, seats):
    results = results
    seats = seats
    parties = list(results.keys())
    seats_per_party = {party: 0 for party in parties}
    while seats > 0:
        max_party = max(results, key=results.get)
        seats_per_party[max_party] += 1
        results[max_party] = results[max_party] / (seats_per_party[max_party] + 1)
        seats -= 1
    return seats_per_party

if __name__ == '__main__':
    results = {
        "A": 100,
        "B": 50,
        "C": 25,
        "D": 10,
    }
    seats = 100
    print(dhondt(results, seats))
