import string

encryptedText = input("Enter the encrypted text: ")
shiftDistance = int(input("Enter the shift distance: "))

allChars = string.printable
plainText = []

for char in encryptedText:
    if char in allChars:
    
        index = allChars.index(char)
      
        newIndex = (index - shiftDistance) % len(allChars)
   
        plainText.append(allChars[newIndex])
    else:
       
        plainText.append(char)


plainText = ''.join(plainText)
print("Decrypted text:", plainText)
