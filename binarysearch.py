arr=list(map(int,input("Enter the sorted array: ").split()))
target=int(input("Enter the number to be searched: "))
 
left = 0
right = len(arr)-1 
mid = (left + right) // 2
while left <=right:
    mid=(left+right)//2

    if target==arr[mid]:
        print("Element found at index: ",mid)
        break
    elif target<arr[mid]:
        right=mid-1
    else:
        left=mid+1
else:
    print("Element not found in the array.")
