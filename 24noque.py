i=100
sum_even=0
sum_odd=0
while i<=500:
    if i%2==0:
        sum_even+=i
    else:
        sum_odd+=i
    i+=1
print("sum_even =",sum_even)
print("sum_odd =",sum_odd)




num1=int(input("enter number"))
num2=int(input("enter number"))
se=0
so=0
if num1>num2:
    while(num2<=num1):
        if num2%2==0:
            se=se+num2
            num2=num2+1
        else:
            so=so+num2
            num2=num2+1
else:
    while num1<=num2:
        if num1%2==0:
            se=se+num1
            num1+=1
        else:
            so+=num1
            num1+=1
print(se)
print(so)