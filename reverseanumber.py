#normal approach.
n=int(input("Enter a number: "))
while n!=0:
    r=n%10
    print(r,end="")
    n=n//10

#math approach.
n=int(input("\nEnter a number: "))
reverse=0
while n!=0:
    r=n%10
    reverse=reverse*10+r
    n=n//10
print("The reverse of the number is: ",reverse)