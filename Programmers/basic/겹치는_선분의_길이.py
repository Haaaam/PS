# 겹치는 선분의 길이
"""
def findoverlap(line1,line2):
    start=max(line1[0],line2[0])
    end=min(line1[1],line2[1])
    return max(0,end-start)

def solution(lines):
    cnt = 0
    # 시작 좌표 기준으로 정렬
    lines=sorted(lines, key=lambda x:x[0])
    print(lines)
    currentline=lines[0]
    for i in range(1,len(lines)):
        nextline=lines[i]
        overlap=findoverlap(currentline,nextline)
        print(overlap)
        cnt+=overlap
        if nextline[1]>currentline[1]:
            currentline=nextline


    return cnt
"""
def solution(lines):

    line = [set(range(min(l), max(l))) for l in lines]
    # &: 교집합, |:합집합
    return len(line[0]&line[1]|line[1]&line[2]|line[0]&line[2])

lines= [[0, 5], [3, 9], [1, 10]]
line=[set(range(min(l),max(l))) for l in lines]

print(len(line[0]&line[1]|line[1]&line[2]|line[0]&line[2]))


"""
for i in range(1,len(lines)):
    if lines[i-1][1]-lines[i][0]!=0 and min(lines[i][1],lines[i-1][1])>max(lines[i][0],lines[i-1][0]):
        line.append([max(lines[i][0],lines[i-1][0]),min(lines[i][1],lines[i-1][1])])
if lines[-1][0]<lines[0][1]:
    line.append([max(lines[-1][0],lines[0][0]),min(lines[-1][1],lines[0][1])])

if len(line)==1:
    print(line[0][1]-line[0][0])

elif not line:
    print(0)

else:
    a,b=line[0][0],line[0][1]
    for i in range(1,len(line)):
        if a>line[i][0]:
            a=line[i][0]
        if b<line[i][1]:
            b=line[i][1]
    print(b-a)
"""
