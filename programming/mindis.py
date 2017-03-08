//Given ‘n’ points in an X-Y plane , write an algorithm and the subsequent Python code to determine the pair of points that are closer. Distance between two points (x1, y1) and (x2, y2) is determined using the formula.



Consider only two decimal places of distance for comparison. When there are multiple points with the same minimum distance print all points.

Input Format

Number of points

x coordinate of point1

y coordinate of point1

x coordinate of point2

y coordinate of point2

…

Output format

Point1 and Point2 that have minimum distance between them//

Solution

n=int(input())
l=[]
min=999
for i in range(n) :
    x=int(input())
    y=int(input())
    l.append((x,y))
for i in range(0,n-1) :
    for j in range(i+1,n) :
        x1,y1=l[i]
        x2,y2=l[j]
        d=(((x2-x1)**2)+((y2-y1)**2))**(0.5)
        if d < min :
            min=d
            m=[]
            m.append((x1,y1))
            m.append((x2,y2))
        elif d==min :
            m.append((x1,y1))
            m.append((x2,y2))
for i in m :
    print(i)
 
