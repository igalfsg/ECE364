# * 0 or more + 1 or more ? one ot zero ^start of string $end of string

import re

inputstuff = '12.21 12.21 aaa  aaaaaa aaaa'

#1
re.match('\s{1}a{2,5}\s{1}', inputstuff)
#2
c = re.subn('[0-9]*\.[0-9]+', "float", inputstuff, count=0)
#3
print (c[1])
#4
suma = 0;
testin = "+45 -45 0 89"
ls = re.findall('[-+]*[0-9]+', testin)
for k in ls:
    suma += int(k)
print (suma)
#5
testin = "EE364 EE364"
c = re.sub('EE364', "EE461", testin, 1)
print(c)
#6
testin = "1.1.1.1"
m = re.match("(^[2][0-5][0-5]|^[0-1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})$",testin)
if (m):
    print("matched")
else:
    print("invalid IP")

re.search("e", input, re.I)
#it checks if the string is equal to e ignoring case
re.match("(.*)(is a)(.*)", input)
#looks for is a with characters around it or without
re.match("(?P<First>.*)(?P<Second>is a)(?P<Third>.*)", input)
#separates the statement puts the stuf in first then puts is a into second and everything after into third
re.search("(I){1}(like){10,}(you){1,2}", input)
#it looks for Ilikelikelikelikelikelikelikelikelikelikeyou or Ilikelikelikelikelikelikelikelikelikelikeyouyou