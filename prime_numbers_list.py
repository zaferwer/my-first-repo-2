number = int(input('please tell me your number :'))
prime = []
for i in range(2,number+1):
    for j in range (2,i//2+1):
        if i/j !=1:
            if i%j==0:
                if i not in prime:
                    break
    else:
        prime.append(i)
print(prime)
