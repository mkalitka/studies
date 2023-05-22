def towers_of_hanoi(n, source, destination, pom):
    if n == 1:
        print("Przenieś krążek z", source, "do", destination)
    else:
        towers_of_hanoi(n - 1, source, pom, destination)
        print("Przenieś krążek z", source, "do", destination)
        towers_of_hanoi(n - 1, pom, destination, source)

towers_of_hanoi(3, "1", "3", "2")
