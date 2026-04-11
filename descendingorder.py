n=int(input("Enter the size of the array: "))
ele=[]
for i in range(n):
    a=int(input("Enter the element: "))
    ele.append(a)

for i in range(n):
    for j in range(i+1,n):
        if ele[i]<ele[j]:
            ele[i],ele[j]=ele[j],ele[i]

print("The descening order is:", ele)
