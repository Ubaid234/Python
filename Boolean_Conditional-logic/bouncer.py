# age = input("How old are you \n")

# if age :
#     # age = int(age) :Don't know y it is giving error
# # 18 - 21 wristband
#   if int(age) >= 18 and int(age) < 21:
#     print("GO through")
# # 21+ Allowed
#   elif int(age) >= 21:
#     print("GET INSIDE THE PUB")
# # less than 18 , not allowed
#   else :
#     print("Try next year")

# else:
#     print("Enter your age")


age = input("How old are you :")
if age:
    age = int(age)
    if age >= 21 :
        print("You are good enough to enter and can drink")
    elif age >= 18:
        print("yOU CAN ENTER , but need a wrist band")    
    else:
        print("You can't come in , try next year")   

else :
    print (" TYPE SOMETHING !") 