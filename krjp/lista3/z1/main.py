def longest_palindromes(s: str):
    palindromes = []
    if len(s) == 0 or len(s) == 1:
        return palindromes
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i : j + 1] == s[i : j + 1][::-1]:
                palindromes.append((i, j - i + 1))
    max_length = max(palindromes, key=lambda x: x[1])[1]
    palindromes = list(filter(lambda x: x[1] == max_length, palindromes))
    return palindromes


if __name__ == "__main__":
    print(longest_palindromes("ostatnio pływałem kajakiem"))
    print(longest_palindromes("anna, zaraz, kajak"))
    print(longest_palindromes("potop, radar, owocowo"))
