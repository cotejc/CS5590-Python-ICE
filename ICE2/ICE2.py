#Jeremiah Cote - Student #1
#ICE 2-Part A
#6/16/2017

print("ICE2-Part A - Determine the number of character frequency in a string")
def number_characters(string1):
    dictionary = {}
    for n in string1:
        keys = dictionary.keys()
        if n in keys:
            dictionary[n] += 1
        else:
            dictionary[n] = 1
    return dictionary
print(number_characters('The quick brown fox jumped over the lazy dog.'))

print('\n')
print("ICE2 - Part B - Determine which word is the longest in the string.")
#Jeremiah Cote - Student #1
#ICE 2-Part B
#6/16/2017
def longest(words):
    length = []
    for n in words:
        length.append((len(n), n))
    length.sort()
    return length[-1][1]
print(longest(["The", "quick", "brown", "fox", "jumped","over", "the", "lazy","dog"]))

#Jeremiah Cote - Student #1
#ICE 2-Part C
#6/16/2017

print("\n")
print("ICE2 - Part C - Determine the number of digits and letters")
user_string = input("Please enter a sentence")
numbers=letters=0
for characters in user_string:
    if characters.isdigit():
        numbers=numbers+1
    elif characters.isalpha():
        letters=letters+1
    else:
        pass
print("Letters", letters)
print("Numbers", numbers)