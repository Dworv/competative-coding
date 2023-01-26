n, m, k = [int(x) for x in input().split()]

k -= n

flag = False

if k < 0:
    flag = True

seq = [1]

while k > 0:
    prev = seq[-1]
    maxk = min(len(seq), m - 1)
    if maxk <= k:
        if len(seq) < m:
            seq.append(prev+1)
        else:
             seq.append(seq[-m])
        k -= maxk
    else:
        seq.append(seq[-k-1])
        k = 0
    if n < len(seq):
        flag = True
        break

seq += [seq[-1]] * (n - len(seq))
if flag: 
    print(-1)
else:
    print(" ".join([str(x) for x in seq]))