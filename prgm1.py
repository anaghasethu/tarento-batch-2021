"""
Given a paragraph count the frequency of vowels and consonants in each word and capitalize the vowels/consonants in each word whose frequency is the highest. If the frequency of vowels and consonants are equal then capitalize the whole word.

Sample Input and Output

Input : Hey! How are you? I hope you are fine.
Output: HeY! HoW ArE yOU? I HOPE yOU ArE FINE.


"""

s = input()
words = s.split(" ")
for word in words:
    vcount = 0
    ccount = 0
    vstring = ""
    cstring = ""
    for letter in word:
          if letter.lower() in "aeiou":
               vcount += 1
               vstring += letter.upper()
               cstring += letter.lower()
               continue
          elif letter in "qwertyuiopasdfghjklzxcvbnm":
               ccount += 1
               cstring += letter.upper()
               vstring += letter.lower()
               continue

    if vcount == ccount:
          print(word.upper(), end=" ")
    elif vcount > ccount:
          print(vstring, end=" ")
    else:
          print(cstring, end=" ")

