from turtle import hideturtle

str = "mississipi"

counter = str.count("s")

str = str.replace("ss", "ox")

index = str.index("p")

def foo(istring):
    p = '0123456789'
    os = ''
    for ch in range(len(istring)):
        if istring[ch] not in p:
            os += istring[ch]
    return os

# print(foo("u8u8u8"))

# def repeat():
#     newstring = []
#     word = input("Enter a word: ")
#     while word != "":
#         for i in range(len(word)):
#             x = word.count(word[i])
#             if x > 1:
#                 add_this_word = word
#         newstring.append(add_this_word)
#         word = input("Enter a word: ")
#     return newstring

def repeat():
    newstring=[]
    newstring2=[]
    word=input("Enter a word: ")
    while word!='':
        for i in (word):
            x=word.count(i)
            if x>1:
                newstring.append(word)
                [newstring2.append(word) for word in newstring if word not in newstring2]
        word=input("Enter a word: ")
    return newstring2

# def is_palindrome(str):
#     str2 = ""
#     for ch in str:
#         if ch.isalpha() == True:
#             str2 += ch
#     print(str2)


import copy

def in_palindrome(possiblepalindrome):
    out = ""
    for ch in possiblepalindrome:
        if ch.isalpha():
            out += ch
    possiblepalindrome = out

    possiblepalindrome = possiblepalindrome.lower()
    str2=possiblepalindrome[::-1]
    print(str2, possiblepalindrome)
    if str2==possiblepalindrome:
        return True
    else:
        return False

# print(in_palindrome("Abba"))
# print(in_palindrome("Telat"))
# print(in_palindrome("MadaM I'm Adam"))

def igpay(word):
    out = ""
    vowel = ["a", "e", "i", "o", "u"]
    consonent = ""
    if word[0] in vowel:
        return word + "way"
    else:
        index = 0
        while(word[index] not in vowel):
            out += word[index]
            index += 1
        xxx = word[index:]
        return xxx + out + "ay"

# def igpay(word):
#     latin=''
#     for i in (word):
#         if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
#             latin+=i
#             if word[0]!='a' or word[0]!='e' or word[0]!='i' or i[0]!='o' or i[0]!='u':
#                 if i!='a' or i!='e' or i!='i' or i!='o' or i!='u':
#                     latin+=i
#                     latin=latin+'ay'
#                     return latin
#             else:
#                 latin=latin+'cay'
#                 return latin

print(igpay('can'))
print(igpay('answer'))
print(igpay('prepare'))
