num=int(input("enter number"))
sum=0
while num>0:
    digit=num%10
    sum=sum+digit
    num=num//10
print("the total sum of digits=",sum)