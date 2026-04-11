n=int(input("Enter the size of the array: "))
a=[]
for i in range(n):
    a.append(input("Enter the string: "))

a.sort(reverse=True)

a.sort(key=lambda x:len(x),reverse=True)
print("The array in descending order is: ",a)
