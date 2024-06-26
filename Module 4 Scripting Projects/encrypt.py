import string

plainText = input("Enter the plaintext: ")
shiftDistance = int(input("Enter the shift distance: "))

allChars = string.printable
encryptedText = []

for char in plainText:
    if char in allChars:
    
        index = allChars.index(char)
       
        newIndex = (index + shiftDistance) % len(allChars)
      
        encryptedText.append(allChars[newIndex])
    else:
      
        encryptedText.append(char)

encryptedText = ''.join(encryptedText)
print("Encrypted text:", encryptedText)
