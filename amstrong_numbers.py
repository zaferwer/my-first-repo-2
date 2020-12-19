input_1 = input('Please enter the number you want to learn if it is a Amstrong number: ')
x_list = [str(i) for i in str(input_1)]
x_set = set(x_list)
float_list={',','.'}
strin = {'q','w','e','r','t','y','u','ı','o','p','ğ','ü','s','d','f','g','h','j','k','l','ş','i','z','x','c','v','b','n','m','ö','ç'}
if x_set&float_list !=set():
    print("Please enter an integer number")
elif x_set&strin !=set():
    print("Do not use any entries other than numeric values")

else:
    x=int(input_1)
    if x<0:
        print(" Please enter a positive number")
    else:
        x_list2 = [int(i) for i in str(x)]
        y=0
        for i in range(len(x_list2)):
            y += x_list2[i-1]**len(x_list2)
        if x==y:
            print(f"{x} is an Armstrong number")
        elif x!=y:
            print(f"{x} is not an Armstrong number")
