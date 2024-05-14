def cal_greatest(x,y,z):                   #find greatest number out of three
  if x>=y and x>=z:
    return x
  if y>=x and y>=z:
    return y
  else:
    return z
a=int(input("Enter input 1:"))
b=int(input("Enter input 1:"))
c=int(input("Enter input 1:"))
f=cal_greatest(a,b,c)
print("The greatest number is ",f)

def cal_convert(c):                     #celcius to Fahrenheit
   f = (((c)*(9/5))+32)
   return f
a=float(input("Enter input:"))
b=cal_convert(a)
print("The celcius to Fahrenheit is ",b)

def print_table(x):                  #printing table
    result=""
    for i in range(1,11):
       result+=f"{x} X {i} = {x*i}\n"
    return result
a=int(input("Enter input:"))
print(print_table(a))

def cal_Sum(x):                         #Sum of natural number
    if x==0:
        return 0
    else:
        return x + cal_Sum(x-1)

n=int(input("Enter natural number:")) 
result=cal_Sum(n)
print(result)


def print_pattern(x):                  #printing pattern using function
    for i in range(x):
        print("* "*(x))
        x=x-1
n=int(input("Enter input:"))
print(print_pattern(n))
  
list=["Harry","Priya","Piyush"]
for name in list:
    print(f"Good Evening,{name}!")

s={}
print(type(s))
