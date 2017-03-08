//Given ‘n’ integers, write an algorithm and the subsequent Python code to print all numbers that are isomorphic to the first number. Two numbers are said to be isomorphic if they have the same number of digits in it and the sets of positions  having the same  digits areequal.. For example:

12321 is isomorphic to 83538 .
Both the  numbers are of length five.  In 12321, positions 2 and 4 have the same digit 2, Positions 1 and 5 have same digit 1. Hence the set of positions having the same digit are {{1,5},{2,4}. Similarly , for the number 83538, the set of positions having the same digit is {{1,5}, {2,4}}.

1232 is not isomorphic to 2342 because set of places having same digits for 1232 is {{2, 4}} and for 2342 is {{1, 4}} (digits are numbered from left to right starting from 1).
12 not isomorphic to 10.
Write a function to check whether two  numbers are isomorphic. If none of the numbers are isomorphic then print ‘No isomorphic’.

Input Format

First line contains the number of elements, n

Next ‘n’ line contains the numbers

Output Format

Print first number in the first line

Next few lines contain the numbers that are isomorphic to first number//

Solution

def iso(a) :
    t=[]
    w=0
    e=a
    while a>0 :
        t.append(a%10)
        a=a//10
        w+=1
    f=1
    g=1
    if q==w :
        for i in range(0,q-1) :
            for j in range(i+1,q) :
                if p[i]==p[j]  :
                    g=0
                    if t[i]!=t[j] :
                        f=0
                        break
    else :
        f=0
    if g==0 and l[0]==e :
        f=1
    elif g==1 :
        f=0
    return(f)
n=int(input())
l=[]
p=[]
y=[]
q=0
for i in range(n) :
    x=int(input())
    l.append(x)
led=l[0]
while led>0 :
    p.append(led%10)
    led=led//10
    q+=1
for z in range(1,n) :
    a=l[z]
    f=iso(a)
    if f==1 :
        y.append(l[z])
if len(y)>0 :
    print(l[0])
    for i in y :
        print(i)
else :
    print('No isomorphic')

