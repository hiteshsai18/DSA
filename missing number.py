numbers=list(map(int,input("Enter the numbers: ").split()))
miss=(numbers[-1]*(numbers[-1]+1)//2)-sum(numbers)
print(miss)
