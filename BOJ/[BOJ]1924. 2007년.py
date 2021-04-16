Day=['SUN','MON','TUE','WED','THU','FRI','SAT']
thirtyone=[1,3,5,7,8,10,12]
thirty=[4,6,9,11]
two=[2]
m,d=map(int,input().split())
res=0
for i in range(1,m):
    if i in thirtyone:
        res+=31
    elif i in thirty:
        res+=30
    else:
        res+=28
res+=d
print(Day[res%7])

