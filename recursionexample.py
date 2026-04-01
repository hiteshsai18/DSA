def fun(n):
    if n>10:
        return n-1
    return fun(fun(n+2))
n=int(input("Enter a number: "))
print(fun(n))

#dry run for n=5.
# fun(5)
# fun(fun(7))
# fun(fun(fun(9)))
# fun(fun(fun(fun(11))))
# fun(fun(fun(10)))
# fun(fun(8))
# fun(8+2)
# 10 return.