i=0
while i<10:

    print("\t""\t""OUR CALCULATOR")
    print(" 1.) ADDITION""\n"" 2.) SUBTRACTION""\n"" 3.) DIVISION""\n"" 4.) MULTIPLICATION""\n"" 5.) Print Table""\n")
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

    elif A==5:
        num =int(input("enter number for table :"))
        for i in range(1,11):
            print (str(num) + " X " + str(i) + " = " + str(i*num))
    

    else:
        print("not in a list ")

    