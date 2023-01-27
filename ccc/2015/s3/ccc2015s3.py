gates = list(range(int(input())))

num_planes = int(input())

total = 0
for _ in range(num_planes):
    index = int(input()) - 1
    visited = []
    availible = True
    while True:
        visited.append(index)
        if gates[index] == index:
            for v in visited:
                gates[v] = index - 1
            break
        if gates[index] == -1:
            availible = False
            break
        index = gates[index]
    if availible:
        total += 1
    else:
        break

print(total)
