for i in range(1,int(input())):

    if i%3==0 and not(i%5==0):
        print('Fizz'),
    elif i%5==0 and not(i%3==0):
        print('Buzz'),
    elif i%5==0 and i%3==0:
        print('FizzBuzz')
    
    else:
        print(i)