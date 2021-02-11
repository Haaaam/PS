r,c=map(int,input().split())
m=[list(input()) for _ in range(r)]

dx,dy=[-1,1,0,0],[0,0,-1,1]
visited=False
def solve():
    global visited
    for i in range(r):
        for j in range(c):
            if m[i][j]=='W':
                for w in range(4):
                    nx,ny=i+dx[w],j+dy[w]
                    if 0>nx or ny<0 or nx>=r or ny>=c:
                        continue
                    if m[nx][ny]=='S':
                        visited=True
if visited==True:
    print(0)
else:
    print(1)
    for i in range(r):
        for j in range(c):
            if m[i][j]=='.':
                m[i][j]='D'
for i in m:
    print(''.join(i))


