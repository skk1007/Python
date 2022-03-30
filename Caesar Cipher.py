#Caesar Cipher 
print("Jacky's Caesar Cipher\n")
try: 
 encrypt=''
 msg1 = input("Message? ").replace(" ","").upper()
 strRef = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
 shift = int(input("Shift? ")) % 26
 resultText=''
 resultText2=''
 print('Encrypt:')

 for letter in msg1:
     if letter in strRef:
         letterIndex=strRef.find(letter)
         resultIndexEncrypt=letterIndex+shift
         if resultIndexEncrypt >26:
             resultIndexEncrypt=resultIndexEncrypt-26
         resultText=resultText+strRef[resultIndexEncrypt]    
     
 print(resultText)

 print('decrypt:')

 for letter in msg1:
     if letter in strRef:
       letterIndex=strRef.find(letter)
       resultIndexDecrypt=letterIndex-shift
       if resultIndexDecrypt<0:
         resultIndexDecrypt=26-(-resultIndexDecrypt)
       resultText2=resultText2+strRef[resultIndexDecrypt]

 print(resultText2)      
except:
    print("Error input.")
    print("Please input valid alphabets for message and number for shifting.")