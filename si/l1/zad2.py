from collections import defaultdict
S = set()

def reconstruct_text(t):
    n = len(t)
    d = [0]*(n+1) # tabela najlepszych wyników dla każdej długości podciągu
    p = [-1]*(n+1) # tabela najlepszych podziałów dla każdej długości podciągu

    for i in range(1, n+1):
        for j in range(i):
            if t[j:i] in S:
                if d[j] + (i-j)**2 > d[i]:
                    d[i] = d[j] + (i-j)**2
                    p[i] = j

    wynik = []
    i = n
    while i > 0:
        j = p[i]
        wynik.append((j, i))
        i = j

    wynik.reverse()

    wynik = [t[j:i] for j, i in wynik]
    return " ".join(wynik)


def main():
    global S
    with open("polish_words.txt", "r", encoding="utf8") as f:
        for line in f:
            S.add(line.strip())

    solutions = []

    with open("zad2_input.txt", "r", encoding="utf8") as f:
        for line in f:
            solutions.append(reconstruct_text(line.strip()))

    with open("zad2_output.txt", "w", encoding="utf8") as f:
        for line in solutions:
            f.write(line + "\n")

if __name__ == "__main__":
    main()
