arr=list(map(int,input("Enter the array elements: ").split()))
num=int(input("Enter a number: "))
ls=[]
for i in range(len(arr)):
    if arr[i]>num:
        ls.append(arr[i])
ls.sort()
print(ls)