# def sorted_string(string):               #question 1 
#     words=string.split()
#     words.sort()
#     new_sorted=" , ".join(words)
#     return new_sorted

# input_string=input("Enter:")
# print(sorted_string(input_string))


# def with_commas(string):                 #question 2
#     result=""
#     for character in string:
#         result+= character+","
#     return result[:-1]

# input_string=input("Enter:")
# print(with_commas(input_string))


# list_fruits=["Apple","Banana","Mango","Grapes"]
# for index,fruits in  enumerate(list_fruits,start=1):              #Enumerate function
#     print(f"{index}. {fruits}")

# sen=input("Enter input :")                        #count words,digits,uppercase,lowercase
# w,d,u,l=0,0,0,0
# s=sen.split()
# w=len(s) 
# for c in sen:
#     if c.isdigit():
#         d=d+1
#     elif c.isupper():
#         u=u+1
#     elif c.islower():
#         l=l+1
# print("No.of words :",w)
# print("No.of Digits:",d)
# print("No.of Uppercase letters:",u)
# print("No.of Lowercase letters:",l)




