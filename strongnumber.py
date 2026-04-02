#strong number.

num=int(input("Enter a number: "))
temp=num
sum=0
while temp>0:       
    r=temp%10
    fact=1
    i=1
    while i<=r:
        fact*=i
    sum=sum+fact
    temp=temp//10

if sum == num:
    print(num, "is a strong number.")
else:
    print(num, "is not a strong number.")