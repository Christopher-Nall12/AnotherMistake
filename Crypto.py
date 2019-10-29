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

def scrambleToDecrypt(cipherText):
    halflength = len(cipherText) // 2
    evenChar = cipherText[halflength:]    # halflength to the end
    oddChar = cipherText[:halflength]      # 0 to the halflength - 1
    plainText = ""

    for i in range(halflength):
        plainText = plainText + evenChar[i]
        plainText = plainText + oddChar[i]

    if len(oddChar) < len(evenChar):
        plainText = plainText + evenChar[-1]

    return plainText