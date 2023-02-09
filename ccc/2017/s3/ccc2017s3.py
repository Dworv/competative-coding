input()
cnt = [None] + [0] * 4000
for num in input().split():
    cnt[int(num)] += 1

max_flen = 0
amt_max = 0
for l in range(2, 4000):
    amt = 0
    for i, f in enumerate(cnt[1:l//2+1]):
        if l / 2 == i + 1:
            amt += f // 2
        else:
            amt += min(f, cnt[l-i-1])
    if amt == max_flen:
        amt_max += 1
    if amt > max_flen:
        max_flen = amt
        amt_max = 1

print(max_flen, amt_max)