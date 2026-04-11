#searching a string element in an array.

arr=input("Enter elements of the array: ").split()
search=input("Enter the element to be searched: ")
found=False
for i in  range(len(arr)):
    if arr[i]==search:
        print("Element found at index:",i)
        found=True
        #break
if not found:
    print("Element not found in the array.")