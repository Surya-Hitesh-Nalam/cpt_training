#Metachars
'''
^ - start of string
$ - end of string
*-occurances
+ - occurances
? - *+
[] - set of ch
()- grouping
\ - escape
. - new line '''

''' code to take a text data and fetch to match the given data
syntax :- re.match(searchedElement,text)'''

'''
import re

text = 'hi students how are you!!!'
se = r'hi students'
output = re.match(se,text)
if output:
    print("Match found for:",output.group())
else:
    print("No match .....")
'''

#single number search
''' 
import re
text = "My number is 53"
match = re.search(r'\d+',text)
print(match.group())
'''


'''
import re
text = input("Enter a string with number:")
matches =list( re.finditer(r'\d+',text))
if len(matches)>=2:
    print("Second number found",matches[1].group())
elif len(matches)==1:
    print("Only one number found",matches[0].group())
else:
    print("No match")
'''

'''
import re
text = input("Enter a sentence with a number:")
n=int(input("Which number you want to extract:"))
matches = re.findall(r'\d+',text)
if len(matches)>=n:
    print(f"{n}th number is:",matches[n-1])
else:
    print("Not found")
'''

'''
email :- suryanalam1234@gmail.com
sUryanalam1234@gmail.com
s_uryanalam1234@gmail.com
s.uryanalam1234@gamil.com
s+uryanalam1234@gmail.com
s$uryanalam1234@gmail.com
'''

'''
import re
email = input("enter a email:")
pattern = r'^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.[a-zA-z]{2,}$'
if re.match(pattern,email):
    print("Valid")
else:
    print("Not valid")
'''

import re
num = input("Enter a phone number:")
#pattern = r'^[6-9]+[0-9]{0,10}$'
pattern = r'^[+]{1,}+[91]+[6-9]\d{9}$'
if re.match(pattern,num):
    print("Valid")
else:
    print("not valid")

#group , if u have a match in data group will exists
import re
text = "Name: Vijay, Age:12"
match = re.search(r'Name:\s(w+),\sAge:\s(\d+)',text)
