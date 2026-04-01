#argument, no return type.

def summate(a,b):
    c = a + b
    print(f"Sum is {c}")

def difference(a,b):
    d = a - b
    print(f"Difference is {d}")

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
summate(a,b)
difference(a,b)