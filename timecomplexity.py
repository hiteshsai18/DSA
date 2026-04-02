#Time complexity.

def expo(a,b):
    if b==0:
        return 1
    elif b%2==0:
        return expo(a,b//2)**2
    else:
        return a*expo(a,b-1)
print(expo(2,10))                   #o(n^2)