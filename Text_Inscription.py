###  write by arit dey  ###

str=input()
encrypted_binary=""
for i in str:
    encrypted_binary+=bin(int(ord(i)))[2:]
li= list(encrypted_binary)
length=len(li)+len(li)%9
for i in range(8,length,9):
    li.insert(i," ")
print(f'Your text : {str}\n\nEncrypted :\n{"".join(li)}\n\n')

###    ("pleces like my code")    ###
