#factorial of a number.

num = int(input("Enter a number: "))
fact = num
while num > 1:
    fact = fact * (num - 1)
    num = num - 1
print("Factorial of the number is: ", fact)   