#move all the zeroes to the start.

arr=list(map(int,input("Enter the array: ").split()))
zero=0
for i in range(len(arr)):
    if arr[i] == 0:
        arr[zero],arr[i]=arr[i],arr[zero]
        zero+=1
print("After moving zeros to the start:", arr)