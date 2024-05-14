n=int(input("Enter number for series (n>2):"))
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
