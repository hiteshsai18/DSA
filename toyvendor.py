mrp=int(input("Enter the MRP of the toy: "))
item=input("E/B/R")
if item=='E' and mrp>1000:
    print(f"The MRP of the toy is : {mrp}")
    print("The discount is : 5%")
    print(f"The price of the toy is : {mrp-mrp*5/100}")
    print(f"The customer saved: {mrp*5/100}")
elif item=='E' and mrp<=1000:
    print("No discount is applicable.")
if item=='B' and mrp>1000:
    print(f"The MRP of the toy is : {mrp}")
    print("The discount is : 8%")
    print(f"The price of the toy is : {mrp-mrp*8/100}")
    print(f"The customer saved: {mrp*8/100}")
elif item=='B' and 500<mrp<=1000:
    print(f"The MRP of the toy is : {mrp}")
    print("The discount is : 50 Rs.")
    print(f"The price of the toy is : {mrp-50}")
    print(f"The customer saved: 50")
elif item=='B' and mrp<=500:
    print("No discount is applicable.")
if item=='R' and mrp>2000:
    print(f"The MRP of the toy is : {mrp}")
    print("The discount is : 20%")
    print(f"The price of the toy is : {mrp-mrp*20/100}")
    print(f"The customer saved: {mrp*20/100} and an electronic toy.")
elif item=='R' and mrp<=2000:
    print("No discount is applicable.")