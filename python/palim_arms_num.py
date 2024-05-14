n=int(input("Enter number:"))
new=n
sum=0
while(n>0):
    num=n%10
    sum=sum+(num*num*num)
    n=n//10
if(new==sum):
    print(new," is an armstrong number")               # 153 is an armstrong number
else:
    print(new," is not an armstrong number")

print()

n=int(input("Enter number:"))
new=n
sum=0
while(n>0):
    num=n%10
    sum=sum*10+num
    n=n//10
if(new==sum):
    print(new," is an Palindrome number")               # 121 is an Palindrome number
else:
    print(new," is not an Palindrome number")
