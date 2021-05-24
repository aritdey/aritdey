li = ("""also,area,army,baby,back,ball,bank,blue,boat,body,book,boom,born,boss,burn,busy,
call,came,camp,cash,chat,chip,city,club,code,cold,cook,cool,king,rock,rool,fire,next,nest,holy""")
list1 = (li.split(","))

import random

a = (random.choice(list1).upper())
b =("".join(sorted(a)).strip())
print('rearrange the word . use any text format like {AAA or aaaa}\n')
print(f"your task word is : - {b}")

chanse = 2 
gauss = 0

while (chanse >= (gauss + 1)):
    print(f'chanse {gauss + 1 }')
    inp = str(input().upper())
    
    if (a == inp):
        print(f"you will WIN {inp} is a right gauss")
        break
    elif (a != inp):
        print(f"Opps your gauss is rong plecse try again")

    gauss = gauss + 1 


print("\n\t\t     © Copyright 2021 Inc.\n\t\t | Proudly made by Arit Dey |\n \t       Terms_of_Service • Privacy_Policy\n\n")
