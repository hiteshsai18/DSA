#searching a num element in an array.

arr=list(map(int,input("Enter elements of the array: ").split()))
search=int(input("Enter the element to be searched: "))
found=False
for i in  range(len(arr)):
    if arr[i]==search:
        print("Element found at index:",i)
        found=True
        #break
if not found:
    print("Element not found in the array.")