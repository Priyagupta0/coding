n = int(input("Enter number to print prime numbers:"))            # Generate Prime number

if n <= 0:
    print("Please enter a positive number")
elif n == 1:
    print("No prime numbers exist up to 1")
else:
    print("Prime numbers up to", n, "are:")
    for num in range(2, n + 1):
       if all(num % i != 0 for i in range(2, num)):
        print(num, end=' ')

print()

n=int(input("Enter number:"))                # Check Prime or not 
flag=0
if(n<=1):
    print(" prime number does not exist from less than 1")
else:
   for i in range(2,n):
      if(n%i==0):
       flag=1
       break
if(flag==0):
    print(n," is a Prime number")
else:
    print(n,"is not a Prime number")
