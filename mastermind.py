#mastermind
import random
lst1 = []
for i in range(4):
 n = random.randint(1,9)
 lst1.append(n)
print("real secret number(for debugging):" +str(lst1))
#___________________________________________________
bool =False
trial=0  
while bool ==False:

  strinput=input("Please input your guess: ") #str
  trial +=1
  lst2=strinput.split(" ")   # str > string list
  for i in range (len(lst2)):   
   lst2[i]=int(lst2[i])
     
  if lst1!=lst2:
      
     count=0  
   # bool =False
     for i in range(0,len(lst1),1):
      for j in range(0,len(lst2),1):
         if lst2[j]==lst1[i]:
             count+=1
             if lst2.index(lst2[j]) ==lst1.index(lst1[i]) :
              hints = lst2.index(lst2[j])
         else:
             j+=1

   
     print("Now " +str(count)+ " digits matches")
     
     #print(str(hints))
     if hints>=0:
      print("You found the right num and position for the index " + str(hints)+" of the secret numbers.\nOnly 1 hint of your first trial will be offered.")
     elif hints<0:
      print("NA")
    # hints=0 
     continue  
  else:
    bool =True
    if bool ==True:
        print("Now all match, you finished!!!")
        print("total trial =" + str(trial))
        
        