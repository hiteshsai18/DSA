#sum of subarray.

arr=list(map(int,input("Enter the array: ").split()))
maxsum=arr[0]
current=arr[0]

for i in range(1,len(arr)):
    current=max(arr[i],current+arr[i])
    maxsum=max(maxsum,current)

print("Maximum sum of subarray is: ",maxsum)