# Coding Strings

# Concatenation
# 2 strings or more and put the together

firstName = "Yuri"
lastName = "tarded"

print(firstName + " " + lastName)

name = firstName + " " + lastName
lastFirst = lastName + " " + firstName

print(name)
print(lastFirst)

# repitition

print("whyyy"*20)
print("o"*20)

def rowYourBoat():
    print("row"*3 + " your boat")
    print("gently down the stream")
    print("merrily"*4 + " life is but a dream")

rowYourBoat()

# Indexing

name = "Roy G Biv"
firstChar = name[0]
print(firstChar)

middleCharIndex = len(name) // 2
print(middleCharIndex)
print(name[middleCharIndex])
print(name[-1])

for i in range(1, len(name)):
    print(name[i])

