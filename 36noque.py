from re import I


num=int(input("enter number"))
num1=int(input("enter number"))
i=0
sum=0
while i<=num1:
    if i%2==0:
        sum+=i
        print(sum)
    i+=1