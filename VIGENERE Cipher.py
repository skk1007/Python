
#Global
strRef = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

lstSquare = []      #Vigenere Square
for i in range(26):
    lstSquare.append(strRef[(i-26):] + strRef[:i])
    print(lstSquare[i])
    
def main():
    print("Welcome to Joseph's Vigenere Cipher, please select function:")
    print(" E - Encrypt Message")
    print(" D - Decrypt Cipher")
    strFunction = input("Function: ").upper()
    print()
    strCipher = input("Cipher?").upper()
    strKey=input("Key?").upper()
    finalKey=strKey*2
    strMessage = strCipher.replace(" ","").upper()
   
    if strFunction == "E":


        print("Cipher: " + encrypt(strMessage, finalKey))
        return
        print("This is encrpyted")
        #Use Encrypt Function
    elif strFunction == "D":
        print("Sorry, this function not yet finish")
        #Use Decrypt Function
    else:
        print("Incorrect Function")
    return
    print("Message: " + encrypt(strMessage, finalKey))
    #PRMHQXPRWHKA
    #PYTHON
    



def encrypt(strMessage:str, finalKey:str) -> (str):
   encrypted = ""
   j=0
   for i in strMessage:
       
        firstline =(strRef.find(i)) 
        rowjump= strRef.find(finalKey[j])
        encrypted += lstSquare[rowjump][firstline]
        j+=1
        
   return encrypted


main()