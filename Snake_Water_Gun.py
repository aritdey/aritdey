
          ##### Note #####

"""
! use ::- SNAKE  ,  WATER  ,  GUN    

! When you see ( No output ) then try try agen 

! sanke killed by gun , water eat by snake , gun killed by water 

"""
 #############$$$$$$$$$$$#############
 
inp = (str(input()))
trop = (inp.upper())
print("your input is :- " + trop)
print()
S = "SNAKE" 

W = "WATER"

G = "GUN"

import random

name_list = ["snake","water","gun"]

choice = random.choice (name_list)

print("Computer choice is :-" + choice)
print()

          ###### SNAKE ######

if (trop == S):

    if (choice == "water") :
        print("you win 👏👏👏")
        
    elif(choice == "snake") :
        print("mach tai 🤝🤝🤝")
        
    elif(choice == "gun") :
        print("you loss 👎🤦👎")

        ##### WATER #####
        
elif (trop == W):

    if (choice == "water") :
        print("mach tai🤝🤝🤝")
        
    elif(choice == "snake") :
        print("you loss 👎 🤦👎")
        
    elif(choice == "gun") :
        print("you win 👏👏👏")

           ##### GUN #####

elif (trop == G):

    if (choice == "water") :
        print("you loss 👎🤦👎")
        
    elif(choice == "snake") :
        print("you win 👏👏👏")
        
    elif(choice == "gun") :
        print("mach tai 🤝🤝🤝")





