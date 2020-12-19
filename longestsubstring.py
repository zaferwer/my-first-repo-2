s = "tmmzuuxt"
number = count = 0
used = {}
for i in range(len(s)):
    if s[i] in used and number <= used[s[i]]:
        number = used[s[i]] + 1
    else:
        count = max(count, i - number + 1)

    used[s[i]] = i
    print(used)
    print(number)
print(count)