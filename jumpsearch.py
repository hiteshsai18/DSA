arr=list(map(int,input("Enter the sorted array: ").split()))
target=int(input("Enter the number to be searched: "))
n=len(arr)
step=int(len(arr)**0.5)
i=0
while i<n and arr[min(i+step-1,n-1)]<target:
    i+=step
for j in range(i,min(i+step,n)):
    if arr[j]==target:
        print("Element found at index:",j)
        break
else:
    print("Element not found in the array.")