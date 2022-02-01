letters = 'abcdefghijklmnopqrstuvwxyz'

def letterToNumber(letter):
    i = 0
    for let in list(letters):
        if letter == let:
            return i
        i += 1

def encrypter(message, key):
    newMessage = ''
    for letter in message:
        newIndex = letterToNumber(letter) + int(key)
        if newIndex > 25:
            newIndex -= 26
        newMessage += letters[newIndex]
    return newMessage

def decrypter(message, key):
    newMessage = ''
    for letter in message:
        newIndex = letterToNumber(letter) - int(key)
        if newIndex < 0:
            newIndex += 26
        newMessage += letters[newIndex]
    return newMessage

whatDo = input('Do you want to encrypt or decrypt a message')
inputing = True
while inputing:
    message = input('What is the message')
    for letter in message:
        if letter not in letters:
            inputing = True
            break
        else:
            inputing = False

while True:
    key = input('What is the key')
    if len(key) != 1:
        continue
    elif key in '123456789':
        break

if whatDo == 'encrypt':
    print(encrypter(message, key))
if whatDo == 'decrypt':
    print(decrypter(message, key))