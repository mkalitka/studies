import urllib.request


def compress(s):
    compressed_text = []
    counter = 1
    for i in range(len(s)):
        if i == len(s) - 1:
            compressed_text.append((counter, s[i]))
        elif s[i] == s[i + 1]:
            counter += 1
        else:
            compressed_text.append((counter, s[i]))
            counter = 1
    return compressed_text


def decompress(compressed_text):
    decompressed_text = ""
    for i in range(len(compressed_text)):
        decompressed_text += compressed_text[i][0] * compressed_text[i][1]
    return decompressed_text


def main():
    text = (
        urllib.request.urlopen("http://www.gutenberg.org/files/1342/1342-0.txt")
        .read()
        .decode()
    )
    compressed_text = compress(text)
    decompressed_text = decompress(compressed_text)
    print(decompressed_text)
    print(compressed_text)


if __name__ == "__main__":
    main()
