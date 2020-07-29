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

