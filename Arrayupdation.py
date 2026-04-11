a=list(map(int,input("Enter the elements of the array:").split()))
print("Array before updation:",a)
index, value=map(int,input("Enter index and value:").split())
a[index]=value
print("Array after updation:",a)