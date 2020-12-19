x = {1, 2, 3}
result = []
for i in x:
    result += [j.union({i}) for j in result]
    result.append({i})
print([{}] + sorted(result, key=len))
