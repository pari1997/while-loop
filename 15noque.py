n=int(input("enter number"))
i=1
a=0
b=1
c=0
print(a+b)
while i<=n:
    c=a+b
    a=b
    b=c
    print(c)
    i+=1