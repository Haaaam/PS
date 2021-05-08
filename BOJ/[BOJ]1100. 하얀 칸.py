#2021.05.08
'''
해설: 가장 왼쪽 위칸(0,0)이 흰색 칸이므로 2로 나눠지는 짝수 줄에서는
흰 검 흰 검 흰 검 흰 검 패턴을 가지고 있고 홀수 줄에서는
검 흰 검 흰 검 흰 검 흰 패턴을 가지고 있다.
그렇기 때문에 짝수 줄에서는 짝수 칸에 해당하는 곳(흰색)에 말이 있을 경우 cnt+=1
홀수 줄에서는 홀수 칸에 해당하는 곳(흰색)에 말이 있을 경우 cnt+=1을 해주면 된다.

'''
chess=[list(input()) for _ in range(8)]
cnt=0

for i in range(8):
    for j in range(8):
        if i%2==0:
            if j%2==0:
                if chess[i][j]=='F':
                    cnt+=1
        elif i%2==1:
            if j%2==1:
                if chess[i][j]=='F':
                    cnt+=1
print(cnt)
