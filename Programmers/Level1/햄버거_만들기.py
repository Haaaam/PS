def solution(ingredient):

    cnt = 0
    # 주의: 빵-야채-고기-빵 이 순서대로 쌓고 이게 완성되면 한개 포장하고 ingredient에서 없애는 방식으로 반복
    stack = []
    for i in ingredient:
        stack.append(i)

        if stack[-4:] == [1, 2, 3, 1]:
            del stack[-4:]
            cnt += 1
    return cnt

# 빵-야채-고기-빵 1-2-3-1

ingredient=[1, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
a=list(map(str,ingredient))
tmp=''.join(a)

cnt=0
stack=[]
for i in ingredient:
    stack.append(i)
    print(stack)
    if stack[-4:]==[1,2,3,1]:
        del stack[-4:]
        cnt+=1
print(cnt)
"""
while 1:
    if len(ingredient) < 4:
        break
    else:
        if '1231' in tmp:
            cnt += tmp.count('1231')
            tmp = tmp.replace('1231', '')
            print(tmp)
        else:
            break
"""

