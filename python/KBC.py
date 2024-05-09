import random

#Question list
def question(comp,user):
    if(comp==0 and user==3):
        print("Correct Answer is 3")
        return 1
    elif(comp==2 and user==4):
        print("Correct Answer is 4")
        return 1
    elif(comp==1 and user==3):
        print("Correct Answer is 3")
        return 1
    elif(comp==3 and user==2):
        print("Correct Answer is 2")
        return 1
    elif(comp==4 and user==4):
        print("Correct Answer is 4")
        return 1
    elif(comp==5 and user==2):
        print("Correct Answer is 2")
        return 1
    elif(comp==6 and user==1):
        print("Correct Answer is 1")
        return 1
    elif(comp==7 and user==4):
        print("Correct Answer is 4")
        return 1
    elif(comp==8 and user==2):
        print("Correct Answer is 2")
        return 1
    else:
        return -1
print("\t\tWelcome to Kaun Banega Crorepati....")
print("\tYou have only 10 second to answer the question.")
print("\t\t\tLet's Begin!!!")
comp=random.randint(0,8)
if(comp==0):
    print("Which city is known as Pink City in India?\n 1. Banglore \n 2.Maysore \n 3.Jaipur \n 4.Kochi")
if(comp==1):
    print("Current Railway Minister of India? \n 1.Mamta Banarjee \n 2.Ram Vilash \n 3.Ashwini Vaishnaw \n 4.Piyush Goyal")
if(comp==2):
    print("Which god is also known as ‘Gauri Nandan’? \n 1.Agni \n 2.Indra \n 3.Hanuman \n 4.Ganesha")
if(comp==3):
    print("When is the National Hindi Diwas celebrated? \n1.13 September \n2.14 September\n3.14 July\n4.15 August")
if(comp==4):
    print("Which one of the following places is famous for the Great Vishnu Temple?\n1.Bordubar, Indonesia\n2.Bamiyan, Afghanistan\n3.Panja Sahib, Pakistan\n4.Ankorvat, Cambodia")
if(comp==5):
    print("The largest Buddhist Monastery in India is located at ? \n1.Sarnath, Uttar Pradesh \n 2.Tawang, Arunachal Pradesh \n 3.Dharmashala, Himachal Pradesh\n4.Gangtok,Sikkim")
if(comp==6):
    print("The National Stadium in Delhi was earlier known by the name?\n 1.Irwin Stadium \n 2.Mountbatten Stadium\n3.Wellington Stadium\n4.Canning Stadium")
if(comp==7):
    print("Which city is known as the Silicon Valley Of India?\n1.Delhi\n2.Mumbai\n3.Chennai\n4.Bangalore")
if(comp==8):
    print("How do you say Hello in French?\n1.Neeche\n2.Bonjour\n3.Namaste\n4.Chor")
user=int(input("write your answer please in Question Sr.No.:"))
score=question(comp,user)
if score== -1:
     print("You Lose!..Try your Luck next time ")  
elif score== 1:
    print("You Won 1 Crore!!!")
