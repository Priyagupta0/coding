import random
def check_game(user,comp):
    if(user==comp):
       return 0
    elif(user==2 and comp==1):
        return -1
    elif(user==1 and comp==0):
       return -1
    elif(user==0 and comp==2):
        return -1
    else:
        return 1
user=int(input("It's your choice ..Enter please(0 for Snake , 1 for water , 2 for Gun):"))
comp=random.randint(0,2)
score=check_game(user,comp)
print("You:",user)
print("Computer:",comp)
if score==0:
    print("It's Draw!!")
elif score==1:
    print("You Won!!")
elif score== -1:
    print("You Lose!!")