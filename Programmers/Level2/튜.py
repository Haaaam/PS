def solution(s):
    s = s[2:-2].split('},{')

    s = sorted(s, key=lambda x: len(x))
    # print(s)
    stack = []
    for idx in s:
        jj = idx.split(',')
        for j in jj:
            if j.isdigit():
                if int(j) not in stack:
                    stack.append(int(j))
    return stack

# 셀수있는 수량의 순서있는 열거 또는 어떤 순서를 따르는 요소들의 모음을 튜플(tuple)
# n개의 요소를 가진 튜플을 n-튜플
# (a1,a2,a3,,,,,, an)

# (2,3,1,2)
# s="{{2},{2,1},{2,1,3},{2,1,3,4}}"

# 중복되는 원소가 없는 튜플 (a1, a2, a3, ,,,, , an)
# {a1},{a1,a2},{a1,a2,a3},,,,,,{a1,a2,a3,a4,,,,an}
# '{', '}'

s="{{123}}"
s=s[2:-2].split('},{')

s=sorted(s,key=lambda x:len(x))
#print(s)
stack=[]
for idx in s:
    jj=idx.split(',')
    for j in jj:
        if j.isdigit():
            if int(j) not in stack:
                stack.append(int(j))
#for idx in s:
#    j=idx.split(',')
#    for jj in j:

#        if int(jj) not in stack:
#            stack.append(int(jj))
print(stack)
    #for j in idx:
    #    if j.isdigit():
    #        if int(j) not in stack:
    #            stack.append(int(j))
#print(stack)

