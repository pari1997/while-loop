a=int(input("enter number")) 
i=2
while i<=a//2:
    if a%i==0:
        print("not a prime number")
        break
    i=i+1
else:
    print("prine number")