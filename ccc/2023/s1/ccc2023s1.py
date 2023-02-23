input()
top = [0] + [bool(int(x)) for x in input().split()]
bottom = [0] + [bool(int(x)) for x in input().split()]

total = 0
for i in range(1, len(top)):
    t, b = False, False
    if top[i]:
        total += 3
        t = True
    if bottom[i]:
        total += 3
        b = True
    if i%2 == 1 and t and b:
        total -= 2
    if t and top[i-1]:
        total -= 2
    if b and bottom[i-1]:
        total -= 2

print(total)