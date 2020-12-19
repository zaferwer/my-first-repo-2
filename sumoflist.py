S = [12, 1, 61, 5, 9, 2]
k = 24
total = 0
# while k != total:
for i in S:
    total += i
    if sum(S) == k:
        break
    if total > k:
        S.remove(i)

print(S)
