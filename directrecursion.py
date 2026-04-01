# Direct recursion.

def nums(n):
    if n==11:
        return
    print(n, end=" ")
    nums(n+1)
n=int(input("Enter a number: "))
nums(n)
