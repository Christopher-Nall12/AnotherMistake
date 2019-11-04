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
# Center    aStr.center(w)     Find the center point of whatever you put into the parenthesis with the (w) being a word or phrase.
# ljust     aStr.ljust(w)      It returns the string left of its justified length/width.
# rjust     aStr.rjust(w)      It returns the string right of its justified length/width.
# upper     aStr.upper()       Converts all lowercase letters into capitals.
# lower     aStr.lower()       Converts all capital letters into lowercase.
# index     aStr.index(item)   It searches for a given element from the list that you give it.
# rindex    aStr.rindex(item)  It searches for the highest index then returns it.
# find      aStr.find(item)    It is used to find an (Item) that you tell it to
# rfind     aStr.rfind(item)   It finds the highest index and does the same as the find string.

Mine = "not yours"
notYours = " mine"

print(Mine + notYours)
string = (Mine + notYours)


print(string)


print(string)
string.center(5, Mine)
print(string.center(5, Mine))

print(str.ljust(Mine, 5, notYours))



# Character Functions
# All Characters have a value, a numeric value.

print(ord('a'))
print(ord('b'))
print(chr(104))
print(chr(20))
print(chr(75))
print(ord('J'))
