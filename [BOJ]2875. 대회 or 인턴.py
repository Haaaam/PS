''' 대회 보낼 인원이 없을 경우
    1) 여자//2
    2) 남자
    대회 보낼 인원이 있을 경우
    (n+m-k)//3'''
n,m,k=map(int,input().split())

print(min(min(n//2,m),(n+m-k)//3))