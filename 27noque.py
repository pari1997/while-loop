n=int(input("enter the range"))
i=1
while i<=n:
    print(i*i,end=",")
    i+=1


i=1
while i<=50:
    print(i*i,end=",")
    if i==30:
        break
    i+=1