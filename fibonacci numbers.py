fibonacci =[1,1]
for i in range(8):
    fibonacci.append(fibonacci[i]+fibonacci[i+1])
print(fibonacci)