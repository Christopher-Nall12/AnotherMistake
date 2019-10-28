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


from mistakes2 import *
print(letterToIndex('a'))

print(indexToLetter(44))