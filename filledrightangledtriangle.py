#with astriskes.
n=int(input("Enter the value of n: "))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

#with numbers.
n=int(input("Enter the value of n: "))
for i in range(n):      
    for j in range(i+1): 
        print(j+1,end=" ") 
    print()