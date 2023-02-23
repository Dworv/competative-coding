num = int(input())
mtns = [int(x) for x in input().split()]
even_cache = [0] * num
odd_cache = [0] * num

for n in range(num):
    lowest = 10**10
    for s in range(num - n):
        if n%2==1:
            even_cache[s] = even_cache[s+1] + abs(mtns[s]-mtns[s+n])
            lowest = min(lowest, even_cache[s])
        else:
            odd_cache[s] = (odd_cache[s+1] if n > 0 else 0) + abs(mtns[s]-mtns[s+n])
            lowest = min(lowest, odd_cache[s])
    print(f"{lowest} ", end = "")

print()