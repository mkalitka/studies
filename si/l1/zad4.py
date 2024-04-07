def opt_dist(bits, D):
    min_wyn = len(bits)

    for start in range(len(bits) - D + 1):
        sub_bits = bits[start:start+D]
        rest_bits = bits[:start] + bits[start+D:]
        countADD = sub_bits.count("0")
        countDEL = rest_bits.count("1")
        min_wyn = min(min_wyn, countADD + countDEL)

    print(min_wyn)
    return str(min_wyn)


def main():
    solutions = []
    with open("zad4_input.txt", "r", encoding="utf8") as f:
        for line in f:
            bits, D = line.split()
            D = int(D)
            solutions.append(opt_dist(bits, D))
        
    with open("zad4_output.txt", "w", encoding="utf8") as f:
        for sol in solutions:
            f.write(sol + "\n")

if __name__ == "__main__":
    main()
