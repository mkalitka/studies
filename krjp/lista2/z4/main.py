import random
import urllib.request


def uprosc_zdanie(tekst, dl_slowa, liczba_slow):
    slowa = tekst.split()
    nowe_slowa = []
    for slowo in slowa:
        if len(slowo) <= dl_slowa:
            nowe_slowa.append(slowo)
    while liczba_slow < len(nowe_slowa):
        nowe_slowa.remove(random.choice(nowe_slowa))
    return " ".join(nowe_slowa)


if __name__ == "__main__":
    tekst = (
        urllib.request.urlopen("http://www.gutenberg.org/files/1342/1342-0.txt")
        .read()
        .decode()
    )
    print(uprosc_zdanie(tekst, 10, 5))
