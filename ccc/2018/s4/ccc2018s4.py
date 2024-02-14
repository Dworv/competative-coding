from functools import cache

weight = int(input())

@cache
def pbs(weight: int) -> int:
    if weight == 1:
        return 1
    sum = 0
    for i in range(2, weight + 1):
        sum += pbs(weight//i)
    return sum

print(pbs(weight))