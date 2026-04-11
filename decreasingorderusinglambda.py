n=int(input("Enter the size of the array: "))
a=[]
for i in range(n):
    a.append(int(input("Enter the element: ")))

a.sort(key=lambda x:-x)
print("The array in descending order is: ",a)

