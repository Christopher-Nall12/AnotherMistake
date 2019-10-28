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

# Slicing and Dicing

print(name[0:3])
print(name[0:10])

print(name[-3])

for i in range(0, len(name)):
    print(name[i])

# Slicing and dicing

print(name[-4:8])

for i in range(0, len(name)+1):
    print(name[0:i])

if "y" not in name:
    print("y is not in name")



# Method     Use example      Explanation
# Center
# ljust
# rjust
# upper
# lower
# index
# rindex
# find
# rfind
# replace

Mine = "not yours"
notYours = " mine"

print(Mine + notYours)
string = (Mine + notYours)

print(string)
string.center(5, Mine)
print(string.center(5, Mine))

print(str.ljust(Mine, 5, notYours))

# Character Functions
# All Characters have a value, a numeric value.

print(ord('a'))
print(ord('b'))
print(chr(104))