print("\t""\t""OUR CALCULATOR")
print(" 1.) ADDITION""\n"" 2.) SUBTRACTION""\n"" 3.) DIVISION""\n"" 4.) MULTIPLICATION""\n")
A = int(input("choose one:"))
if A==1:
    a=float(input("Enter value :"))
    b=float(input("Enter value :"))
    c=a+b
    print(c)

elif A==2:
    a=float(input("Enter value :"))
    b=float(input("Enter value :"))
    c=a-b
    print(c)

elif A==3:
    a=float(input("Enter value :"))
    b=float(input("Enter value :"))
    c=a/b
    print(c)

elif A==4:
    a=float(input("Enter value :"))
    b=float(input("Enter value :"))
    c=a*b
    print(c)

else:
    print("not in a list ")