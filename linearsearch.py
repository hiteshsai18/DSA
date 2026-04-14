arr=list(map(int,input("Enter the elements: ").split()))
target=int(input("Enter the number to be searched: "))
for i in range(len(arr)):
    if arr[i]==target:
        print("Element found at index:",i)
        break
else:
    print("Element not found in the array")