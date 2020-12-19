def myAtoi(s: str):
    for i in s:
        l = s.split()
    if len(s) == 0:
        return 0
    else:
        for k in l:
            if k == " ":
                l.remove(k)
        try:
            float(l[0])
            check = True
        except:
            check = False
        if len(l) == 0:
            return 0
        if l[0].isdigit() or l[0].lstrip("-").isdigit() or check:
            if "." in l[0]:
                x = int(float(l[0]) // 1)
            else:
                x = int(l[0])
            print(x)
            if x <= 2 ** 31:
                return x
            if x >= (2 ** 31):
                return 2 ** 31
            if x <= -(2 ** 31):
                return -(2 ** 31)
        else:
            return 0


print(myAtoi(" "))
