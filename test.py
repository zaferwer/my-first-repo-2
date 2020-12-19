def superReducedString(s):
    newlist=list(s)
    result=[]
    for i in newlist:
        if newlist.count(i)%2==0:
            for j in range(newlist.count(i)):
                newlist.remove(i)
        elif i not in result:
            result.append(i)
    r=str(''.join(map(str, result)))
    if len(r)==0:
        print("Empty String")       
    else:
        print(r)


s = input()
superReducedString(s)

    

 
