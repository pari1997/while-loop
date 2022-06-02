num=int(input("enter number"))
revers_num=0
while num!=0:
    digit=num%10
    print(digit)
    revers_num=revers_num*10+digit
    print(revers_num)
    num=num//10
print("revers number"+str(revers_num))
if num==revers_num:
    print("palindrome")