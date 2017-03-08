//Given the position of a Rook and a queen in a chess board (8X8 board),  write an algorithm and the subsequent Python code to determine the common positions where both rook and queen can be placed in the next move. Rook can move through any number of cells,  either horizontally or vertically. Queens can move through any number of cells,  either horizontally, vertically or diagonally.  Each cell in the chess board may be represented as a 2-tuple (row,col). For example, if the current position of the rook is (3,1) then the next possible position of the rook may be either in the same column {(2,1),(1,1),(4,1),(5,1),(6,1),(7,1),(8,1)} or in the same row {(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(3,8)}. If the queen is in the position (5,3) then it can be placed in the same row {(5,1),(5,2),(5,4),(5,5),(5,6),(5,7),(5,8)} or same column {(1,3),(2,3),(3,3),(4,3),(6,3),(7,3),(8,3)} or along the diagonal of the current position {(6,4),(7,5),(8,6),(4,2),(5,1),(6,2),(7,1),(4,4),(3,5),(2,6),(1,7)}. Then the common cells for next move are {(3,3), (5,1), (7,1)}.

The output is a set of common board positions where both queen and rook can be placed. The positions must be printed in sorted order, sort it by row. When rows are same,  sort it by column.

(Hint: Use built-in function to sort the values)

Input Format

Row position of rook

Column position of rook

Row position of queen

Column position of queen

Output Format

Common position1

Common position2

…//

Solution

r={0}
r2={0}
xr=int(input())
yr=int(input())
xq=int(input())
yq=int(input())
s1=xq+yq
a=xq-yq
b=yq-xq
for i in range(1,9) :
    r2.add((xr,i))
    r2.add((i,yr))
r2=r2-r
r2=r2-{(xr,yr)}
q={0}
q2={0}
for i in range(1,9) :
    for j in range(1,9) :
        if i+j==s1 :
            q2.add((i,j))
        elif xq>yq :
            if i-j==a :
                q2.add((i,j))
        elif yq>xq :
            if j-i==b :
                q2.add((i,j))
for i in range(1,9) :
    q2.add((xq,i))
    q2.add((i,yq))
q2=q2-q
q2=q2-{(xq,yq)}
a=r2&q2
c=list(a)
c.sort()
for i in c :
    print(i)
