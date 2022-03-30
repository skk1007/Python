
#lab13 asm by 55208188 WONG SAI KIT 
print("Welcome to Jacky's Mastermind solver! ")
secret=(input("Please input your secret number: " )) #'1234'

lstsecret = str(secret) #'1234'

intguess=1111
lstguess=str(intguess) #'1','1','1','1'
answer=['1','1','1','1']
correct=0
trial =0
#print(answer)
print('')
for j in range(4):
    correct+=1
    for i in lstsecret:
       if i ==lstsecret[j]:
           answer[j]=i
          
           
           print("you got "+ str(correct) +" correct!")
           print( str(answer))
           trial+=1
print("")           
print("Total trial : " + str(trial))      

print("Please press enter to end the program")     
#print(str(answer))          



 
