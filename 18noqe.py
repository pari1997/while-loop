n=int(input("enter binary number"))
sum=0
i=0
while n!=0:
    rem=n%10
    sum=sum+rem*pow(2,i)
    print(sum)
    n=(n/10)
    i=i+1
print("decimal number",sum)