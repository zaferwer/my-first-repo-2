n = int(input())
h = list(map(int, input().rstrip().split()))
result = []
reverseh = h[::-1]
total = 0
for i in range(n):
    result.append(min(h[i:]) * (n - i))
    result.append(min(reverseh[i:]) * (n - i))
    if h[i] >= h[i + 1]:
        total += h[i]
    result.append(total)
print(max(result))