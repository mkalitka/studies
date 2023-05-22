import random

#ex = "abc+bc(dab(cc)*)*+(a+b)*"
ex = input()

def rand(k):
    x = random.random()
    y = 1 - x
    z = int(k * ((1/y) - 1))
    return z

parts = []
is_inside_bracket = False
start_index = 0
for i in range(len(ex)):
    if ex[i] == "(":
        is_inside_bracket = True
    if ex[i] == ")":
        is_inside_bracket = False
    if i == len(ex) - 1:
        parts.append(ex[start_index:])
    if ex[i] == "+" and is_inside_bracket == False:
        parts.append(ex[start_index:i])
        start_index = i + 1

print(random.choice(parts))
print(rand(123132))
