nums = [3, 4, -1, 1]
result = []
if 1 not in nums:
    return 1
else:
    for i in nums:
        if (i + 1) not in nums and i > 0:
            result.append(i + 1)
    return min(result)
