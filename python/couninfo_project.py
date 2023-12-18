print("\t\t""HI EVERYONE")
print("\t\t""welcome in coun_info")
print("So,which country information you want to know?")
print("Here,In our list")
print("1. INDIA""\n""2. PAKISTAN""\n""3. NEPAL""\n""4. CHINA""\n")
country_info={"India":["National Capital:New Delhi" ,  "National Currency: Rupee"  ,  "Common Language spoken:Hindi,English"  ,  "Famous place: Taj Mahal(A UNESCO World Heritage Site)"],"Pakistan":["National Capital:Islamabad" , "National Currency:Rupee" , "Language Spoken:Urdu" , "Famous Place:Lahore Fort(UNESCO World Heritage Site)"],"Nepal":["National Capital:Kathmandu" , "National currency: Nepalese rupee" , "Language Spoken:Nepali" , "Famous Place:The Mount Everst,Lumbini(Birthplace of Buddha, UNESCO World Heritage Site)"],"China":["National capital:Beijing" , "National Currency:Yen" , "Language Spoken:Chinese"  , "Famous place:Great Wall of China(A UNESCO World Heritage Site)"]}
A = int(input("choose one:"))
if A==1:
        print(country_info["India"])
elif A==2:
        print(country_info["Pakistan"])
elif A==3:
        print(country_info["Nepal"])
elif A==4:
        print(country_info["China"])
else:
        print("not in a list")
