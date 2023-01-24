T = int(input())

for _ in range(T):
    N = int(input())
    mountain = [int(input()) for _ in range(N)]
    branch = []
    out = "Y"
    n = 1
    while True:
        if len(mountain) > 0 and len(branch) > 0:
            if mountain[-1] == n:
                n += 1
                mountain.pop()
            elif branch[-1] == n:
                n += 1
                branch.pop()
            else:
                if mountain[-1] < branch[-1]:
                    branch.append(mountain.pop())
                else:
                    out = "N"
                    break
        elif len(mountain) > 0:
            if mountain[-1] == n:
                n += 1
                mountain.pop()
            else:
                branch.append(mountain.pop())
        elif len(branch) > 0:
            if branch[-1] == n:
                n += 1
                branch.pop()
            else:
                out = "N"
                break
        else:
            break
    print(out)