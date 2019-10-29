# Transposition Cypher

# encryption first

def scrambleToEncrypt(plaintext):
    evenChar = ""
    oddChar = ""
    charCount = 0
    for ch in plaintext:
        if charCount % 2 == 0:
            evenChar = evenChar + ch
        else:
            oddChar = oddChar + ch
        charCount = charCount + 1
    cipherText = oddChar + evenChar
    return cipherText

from mistakes2 import *

