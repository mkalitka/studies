def is_palindrom(text):
    text = text.lower()
    processed_text = []
    for i in range(len(text)):
        if text[i] not in " .,:;!?":
            processed_text.append(text[i])
    processed_text = "".join(processed_text)
    return processed_text == processed_text[::-1]


if __name__ == "__main__":
    print(is_palindrom("Kobyła ma mały bok."))
    print(is_palindrom("Eine güldne, gute Tugend: Lüge nie!"))
    print(is_palindrom("Míč omočím."))
    print(is_palindrom("Ząb zupa zębowa;"))

