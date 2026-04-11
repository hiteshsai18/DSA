#rotate an array to the right by 1 step.
arr=list(map(int,input("Enter the array elements: ").split()))
last_element = arr[-1]
for i in range(len(arr) - 1, 0, -1):
    arr[i] = arr[i - 1]
arr[0] = last_element
print("Rotated array:", arr)