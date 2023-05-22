def sasiedzi(mapa, pos_x, pos_y, mark):
    if mapa[pos_y][pos_x] == "#" or mapa[pos_y][pos_x] == mark:
        return mapa
    else:
        mapa[pos_y][pos_x] = mark
    mapa = sasiedzi(mapa, pos_x + 1, pos_y, mark)
    mapa = sasiedzi(mapa, pos_x - 1, pos_y, mark)
    mapa = sasiedzi(mapa, pos_x, pos_y - 1, mark)
    return sasiedzi(mapa, pos_x, pos_y + 1, mark)

x = input("x: ")
y = input("y: ")
mapa = []
for i in range(int(y)):
    l = []
    l[:0] = input()
    mapa.append(l)
    print(mapa)

num = 0
for i in range(int(y)):
    for j in range(int(x)):
        if mapa[i][j] == ".":
            mapa = sasiedzi(mapa, j, i, num)
            num += 1

for i in range(int(y)):
    for j in range(int(x)):
        print(mapa[i][j], end="")
    print()
