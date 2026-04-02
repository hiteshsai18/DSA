#niven's number.

def is_niven_number(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit
        temp //= 10

    if num % sum == 0:
        print(num, "is a Niven's number")
    else:
        print(num, "is not a Niven's number")

num_input = int(input("Enter a number: "))

is_niven_number(num_input)
