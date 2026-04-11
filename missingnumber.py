arr=list(map(int,input("Enter the array elements: ").split()))
num=int(input("Enter total number count:"))
e_sum=num*(num+1)//2
a_sum=sum(arr)
print("Missing number:",e_sum-a_sum)