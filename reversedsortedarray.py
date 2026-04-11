#reverse and sort an array.

arr=list(map(int,input("Enter the aray elemnents:").split()))
start=0
end=len(arr)-1
while start<end:
    arr[start],arr[end]=arr[end],arr[start]
    start+=1
    end-=1

print(arr)