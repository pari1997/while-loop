n=int(input("enter number"))
s=0
sp=1
sn=0
i=2
while i<=n:
    if i%2==0:
        sp=sp+i**2
        i+=1
    else:
        sn=sn+i**2
        i+=1
    print(sp-sn)