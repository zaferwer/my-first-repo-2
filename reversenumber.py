def reverse(x):
    if x >= 0 and x < 4294967296:
        strx = str(x)
        newxlist = "" + strx[::-1]
        result = int(newxlist)
    if x < 0:
        strx = str(-x)
        newxlist = "" + strx[::-1]
        result = 0 - int(newxlist)
    if x > 2 ** 31 or result > 2 ** 31 or x < -(2 ** 31) or result < -(2 ** 31):
        return 0
    else:
        return result


print(reverse(-54545454588787978))