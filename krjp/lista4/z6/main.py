def reconstruct_shadow(shadow):
    if len(shadow) != 2 and len(shadow[0]) != len(shadow[1]):
        return None

    image = []
    for i in range(len(shadow[0])):
        image.append([0] * len(shadow[0]))

    for i in range(len(shadow[0])):
        for j in range(len(shadow[1])):
            if shadow[0][i] > 0 and shadow[1][j] > 0:
                image[j][i] = 1
                shadow[0][i] -= 1
                shadow[1][j] -= 1

    for s in shadow:
        for i in s:
            if i != 0:
                return None

    result = ""
    for i in image:
        for j in i:
            result += str(j) + " "
        result += "\n"
    return result


print(reconstruct_shadow([[2, 1, 3, 1], [1, 3, 1, 2]]))
print(reconstruct_shadow([[2, 3, 0, 4, 1], [3, 3, 2, 1, 1]]))
