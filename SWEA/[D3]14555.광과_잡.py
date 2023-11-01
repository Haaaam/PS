# 공은 열린 괄호와 닫힌 괄호가 붙어있는 '()'로 표현, 서로 다른 두 공이 겹치지 않는다
# 잡초가 자라서 몇 개의 칸이 가려지게 되어 있다. 잡초는 '|'로 표현
# 초원에 놓았을 수 있는 공의 최솟값 return

tc=int(input())
# 공의 개수의 최솟값을 구하는 프로그램 작성
for j in range(tc):
    s=input()
    answer=0
    for i in range(1,len(s)):
        if s[i-1]=='(':

            if s[i]=='|' or s[i]==')':
                answer+=1

        elif s[i]==')':
            if s[i-1]=='|':
                answer+=1

    print(f"#{j+1} {answer}")