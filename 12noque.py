from itertools import product


num=int(input("enter number"))
n=num
product=1
while n!=0:
    rem=n%10
    product*=rem
    n//=10
    print("n=",n)
print(product)



num=int(input("enter number"))
i=1
pro=1
while i<=num:
    num1=int(input("enter number"))
    pro=pro*num1
    i+=1
print(pro)