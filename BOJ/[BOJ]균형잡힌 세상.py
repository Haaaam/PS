# 세계는 균형이 잘 잡혀있어야 한다.
# 왼쪽 괄호와 오른쪽 괄호처럼
#  괄호: 소괄화("()"), 대괄호("[]")로 2종류, 문자열이 균형을 이루는 조건

while True:
    s=input()
    stack=[]
    check=True
    if s==".":
        break

    for i in s:
        if i=="(":
            stack.append(i)

        elif i=="[":
            stack.append(i)

        elif i==")":
            if len(stack)==0:
                check=False
                break
            if stack.pop()!="(":
                check=False
                break



        elif i=="]":
            if len(stack)==0:
                check=False
                break
            if stack.pop()!="[":
                check=False
                break


    # 균형 이룬 경우
    if len(stack) == 0 and check==True:
        print("yes")

    # 균형 X
    else:
        print("no")


