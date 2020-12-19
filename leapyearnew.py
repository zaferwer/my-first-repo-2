x = int(input('please enter the year ypu want to check if it is a leap year :'))
if x%4==0 and x%100!=0 or  x%400 ==0 :
    print(x,'is a leap year')
else:
    print(x,'is NOT a leap year')