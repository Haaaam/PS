# 자연수 n이 있다. n의 10진법 표기에서 나타나는 숫자들을 재배열하여 n보다 큰 n의 배수를 만들 수 있는지 판단하는 프로그램 작성
import itertools
t=int(input())
for i in range(t):
    s=input()
    res="impossible"
    for j in itertools.permutations(s,len(s)):
        tmp=''
        for idx in j:
            tmp+=idx
        if int(tmp)>int(s) and int(tmp)%int(s)==0:
            res="possible"
            break

    print(f"#{i+1} {res}")
