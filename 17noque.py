a=(input("enter number"))
i=0
l=len(a)
armstrong=0
while  i<l:
    k=(int(a[i]))
    b=k**l
    armstrong=b+armstrong
    print(armstrong)
    i+=1
if armstrong==int(a):
    print("armstrong")
else:
    print("not armstrong")





























a=input("enter number")
i=0
digit=len(a)
sum=0
while i<len(a):
    b=a[i]
    c=(int(b)**3)
    sum+=c
    i+=1
if int(a)==sum:
    print("polindrome")
else:
    print("not polindrome")