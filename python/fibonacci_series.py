n=int(input("Enter number for series (n>2):"))               #Fibonacci series
x1=0
x2=1
if(n<0):
    print("Enter positive number")
elif(n==1):
    print("Fibonacci series:",x1)
elif(n==2):
    print("Fibonacci series:",x1,x2)
else:
    print("Fibonacci series:",x1,x2,end=' ')
    for n in range(n):
      x=x1+x2
      x1=x2
      x2=x
      print( x,end=" ")

print()

def is_fibonacci(n):                      # Check number is fibonacci number or not
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

number = int(input("Enter number: "))
if is_fibonacci(number):
    print(number, "is a Fibonacci number.")
else:
    print(number, "is not a Fibonacci number.")
