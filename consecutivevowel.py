x = "zafeer"
xlist = list(x)
vowels = ["a", "e", "i", "o", "u"]
result = 1
res = 0
for i in range(len(xlist) - 1):
    if xlist[i] in vowels and xlist[i + 1] in vowels:
        result = 0
        res = 1
print("negative" * result or "positive" * res)
