//Write an algorithm and write the Python code to count the number of unique words in a given passage. The paragraph may contain words with special characters such as ‘!’, ‘?’, ‘.’, ‘,’ , ‘:’ and ‘;’ and digits are not permitted. Special character must occur only at the end of a word in a passage that is Hello World! is valid but Hello !World or Hello Wor!ld is invalid. No two special character occur together. Print ‘Invalid input’ for such cases. Count words without special characters. Counting must be case insensitive. Print words in lower case and in sorted order. For example, given a passage ‘Programming is a skill in demand! Your programming skills are bankable assets.’ The output should be

{‘a’: 1,

‘are’: 1,

‘assets’: 1,

‘bankable’: 1,

‘demand’: 1,

‘in’: 1,

‘is’: 1,

‘programming’: 2,

‘skill’: 1,

‘skills’: 1,

‘your’: 1}

[Hint: use pprint function for printing dictionary in sorted order.

Syntax for pprint is

pprint(dictionary name)

Include the line “from pprint import pprint” in the top of your program]

Input format:

enter a paragraph

Output format:

Dictionary of words in the passage and their count

Boundary conditions:

One paragraph is entered at a strech//

Solution

import pprint
w=str(input())
l=w.split()
t=[]
d={}
f=1
for i in l :
    k=''
    for j in i :
        k+=j.lower()
    t.append(k)
for i in t :
    if i.isalpha() :
        if i in d :
            d[i]+=1
        else :
            d[i]=1
    elif i[:len(i)-1].isalpha() :
        i=i[:len(i)-1]
        if i in d :
            d[i]+=1
        else :
            d[i]=1
    else :
        f=0
        break
if f==1 :
    pprint.pprint(d)
else :
   print('Invalid input')
