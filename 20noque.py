
num1=(input("enter nmbr"))
r=0
i=0
while i<len(num1):
    r=r+int(num1[i-1])
    print(r,end="")
    i-=1