alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(inputText,shiftNumber):
    cipherText=""
    for letter in inputText:
        position = alphabet.index(letter)
        newPosition=position+shiftNumber
        newLetter = alphabet[newPosition]
        cipherText += newLetter
    print(f"The encoded message is {cipherText}")
def decrypt(inputText,shiftNumber):
    decipheredTest=""
    for letter in inputText:
        position = alphabet.index(letter)
        newPosition=position-shiftNumber
        newLetter = alphabet[newPosition]
        decipheredTest += newLetter
    print(f"The decoded message is {decipheredTest}")

if (direction=="encode"):    
    encrypt(text,shift)
elif(direction=="decode"):
    decrypt(text,shift)
else:
    print("Wrong Input")