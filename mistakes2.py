def letterToIndex(letter):
    from string import ascii_lowercase
    alphabet = ascii_lowercase + ' '
    idx = alphabet.find(letter)
    if idx == -1:       # Means it wasnt in the alphabet
        print("error", letter, "is not in the alphabet")
    return idx

def indexToLetter(idx):
    from string import ascii_lowercase
    alphabet = ascii_lowercase + ' '
    letter = ''
    if idx >= len(alphabet):
        print("error", idx, "is to large")
    elif idx < 0:
        print("error", idx, "is to small")
    else:
        letter = alphabet[idx]
    return letter




from Crypto import *

print(scrambleToEncrypt("The Meeting is at five oclock"))
print(scrambleToDecrypt("h etn sa ieolcTeMeigi tfv cok"))



# write an cesarEncrypt(plainText, shift)
# write an cesarDecrypt(plainText, shift)


def encryptMessage():
    mg = input("enter your message here to encrypt: ")
    cypherText = scrambleToEncrypt(mg)
    print("the encrypted message is:", cypherText)

print(encryptMessage())

def cesarEncrypt():
    input("Message:")
    if "a" :print("c")
    if "b" :print("f")
    if "c" :print("e")
    if "b" :print("f")
    if "c" :print("g")

print(cesarEncrypt())


def cesarCipher(val):
    input("Message:")
    Encryption = ""
    for E in val:
        num = ord(E)

        if num == 122:
            newnum = 97
        elif num == 90:
            newnum = 65
        else:
            newnum = num + 1

        Encryption = Encryption + chr(newnum)

    return Encryption

print(cesarCipher('10'))


alphabet = "abcdefghijklmnopqrstuvwxyz"

def cesar(word):
    encoded = ""
    for ch in word:
        index = alphabet.find(ch)
        nextIndex = (index + 3) % 26
        encoded += alphabet[nextIndex]
    return encoded

print(cesar("hello"))