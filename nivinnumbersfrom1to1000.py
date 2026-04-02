for num in range(1, 1000):
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