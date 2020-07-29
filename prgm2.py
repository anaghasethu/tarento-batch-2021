
#- Accept a String input
#- Accept a search String to search in the above input
#- Verify if the search String is present in the input string and the position and number of occurrences
#Eg. If the String input is - I like reading about threading and the search String is read then the output should be as below
#Occurrences - 2
#Position - 8,24

import re

st = raw_input("String Input>>");
search = raw_input("Search Input>>");

print 'Occurrences - ',st.count(search);


for match in re.finditer(search, st):
    s = match.start()
    print 'Position - ',s+1


