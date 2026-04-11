num=int(input("Enter the distance you want to travel: "))
if num<=0:
    print("The ride cannot be initiated.")
if num>0 and num<=5:
    print(f"The fare is : {num * 6}")
if num>5 and num<=10:
    print(f"The fare is : {(num-5) * 7 + 30}")
if num>10 and num<=18:
    print(f"The fare is : {(num-10) * 8 + 65}")
if num>18 and num<=30:
    print(f"The fare is : {(num-18) * 9 + 129}")
if num>30:
    print("The ride is not possible.")