nums = [3, 3]
target = 6


def twoSum(nums, target):
    result = []
    new = nums.copy()
    for i in nums:
        new.remove(i)
        if (target - i) in new:
            first = i
            result.append(nums.index(first))
            break
    second = target - first
    if first == second:
        result = [index for index, v in enumerate(nums) if v == first]
    else:
        result.append(nums.index(second))
    print(result)


twoSum(nums, target)
